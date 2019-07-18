from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

import uuid


# Se definen los modelos de nuestra base de datos


class Cliente(models.Model):
    # Modelo que contiene los datos de los Clientes de la Empresa.

    idCliente = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Identificador unico para el cliente")
    nombre = models.CharField(max_length=50, help_text="Ingrese el nombre del cliente")
    rubro = models.CharField(max_length=50, help_text="Ingrese rubro en el que se desempena el cliente")
    direccion = models.TextField(max_length=200, help_text="Ingrese la direccion del cliente")
    contacto = PhoneNumberField(help_text="Ingrese nro de contacto del Empleado")
    observacion = models.TextField(max_length=1000, help_text="Observaciones", null=True)

    def __str__(self):
        # String que representa a al Cliente
        return self.nombre


class Proyecto(models.Model):
    # Modelo que contiene datos sobre el Proyecto

    nombre = models.CharField(max_length=30, help_text="Ingrese el nombre del proyecto")
    cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True)
    encargado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='encargado')
    tipo = models.CharField(max_length=100, help_text="Ingrese el tipo del trabajo a ejecutar")
    observacion = models.TextField(max_length=1000, help_text="Observaciones", null=True)

    def __str__(self):
        # String que representa a al Cliente
        return '%s, %s' % (self.nombre, self.cliente)

    def get_cliente(self):
        return self.cliente


class Team(models.Model):
    # Modelo que contiene los datos de cada Team encargado de ejecutar una tarea

    nombre = models.CharField(max_length=10, unique=True, help_text="Ingrese el nombre del Team", default="")
    usuarios = models.ManyToManyField(User, help_text="Seleccione empleados que conforman este team", default="")
    teamLeader = models.ForeignKey(User, help_text="Seleccione el lider del Team", on_delete=models.SET_NULL,
                                   null=True, related_name='teamLeader')

    @property
    def display_users(self):
        users = self.usuarios.all()

        return ', '.join(users.username for users in self.usuarios.all()[:3])

    def __str__(self):
        # String que representa a al Usuario
        return self.nombre


class Vehiculo(models.Model):

    # Modelo que contien datos sobre los vehiculos de la empresa

    marca = models.CharField(max_length=30, help_text="Ingrese la marca del vehiculo")
    modelo = models.CharField(max_length=30, help_text="Ingrese el modelo del vehiculo")
    nroPatente = models.CharField(max_length=6, help_text="Ingrese el numero de chapa del Vehiculo", unique=True)
    fechaMantenimiento = models.DateField(help_text="Ingrese la fecha del ultimo mantenimiento realizado al Vehiculo")
    kmMantenimiento = models.IntegerField(help_text="Ingrese el kilometraje del vehiculo al momento del ultimo "
                                                    "mantenimiento")
    kilometraje = models.IntegerField(help_text="Ingrese el kilometraje actual")

    def __str__(self):
        # String que representa a al Usuario
        return '%s, %s, %s' % (self.marca, self.modelo, self.nroPatente)


class Tarea(models.Model):
    # Modelo que contiene datos de las tareas a ser ejecutadas dentro de un proyecto

    idTarea = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Indentificador unico de la Tarea")
    descripcion = models.TextField(max_length=200, help_text="Ingrese una beve descripcion de la tarea a ejecutar")
    fechaIni = models.DateField(help_text="Ingrese la fecha de inicio de la ejecucion de la tarea")
    fechaFin = models.DateField(help_text="Ingrese la fecha de finalizacion de la ejecucion de la tarea")
    proyecto = models.ForeignKey(Proyecto, help_text="Seleccione el proyecto al cual esta asociada esta tarea",
                                 on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(Team, help_text="Seleccione el team encargado de ejecutar la tarea",
                             on_delete=models.SET_NULL, null=True)
    observacion = models.TextField(max_length=1000, help_text="Observaciones", null=True, blank=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True, help_text="Seleccione el vehiculo"
                                                                                           "utilizado para la tarea")

    def vehiculos(self):
        return self.vehiculo.__str__()

    def __str__(self):
        # String que representa a al Usuario
        return self.descripcion


class Transaccion(models.Model):

    # Modelo que contiene todos los datos de las transacciones realizadas para la ejecucion de una tarea

    tarea = models.ForeignKey(Tarea, help_text="Seleccione la tarea asociada a la trasaccion", on_delete=models.SET_NULL
                              , null=True)

    TRANSACCION_TIPO = (
        ('m', 'Transaccion Madre'),
        ('a', 'actualizacion')
    )

    tipo = models.CharField(max_length=1, choices=TRANSACCION_TIPO, blank=True, default='m',
                            help_text='Seleccione tipo de transaccion')
    nroTransaccion = models.IntegerField(help_text="Ingrese el numero de transaccion bancaria provehido por el banco",
                                         blank=True, null=True)
    combustible = models.IntegerField(help_text="Ingrese el monto a transferir para compra de combustible", default=0)
    viatico = models.IntegerField(help_text="Ingrese el monto a transferir para viaticos", default=0)
    hospedaje = models.IntegerField(help_text="Ingrese el monto a transferir para hospedaje", default=0)
    peaje = models.IntegerField(help_text="Ingrese el monto a transferir para peajes", default=0)
    imprevistos = models.IntegerField(help_text="Ingrese el monto a transferir para gastos imprevistos", default=0)
    ESTADO = (
        ('a', 'Abierta'),
        ('c', 'Cerrada')
    )
    estado = models.CharField(max_length=1, choices=ESTADO, default='a', blank=True)
    fecha = models.DateField(help_text="Ingrese fecha de realizacion de la transaccion")
    observacion = models.TextField(max_length=1000, help_text="Observaciones", blank=True, null=True)

    def __str__(self):
        # String que representa a al Usuario
        return self.tarea.__str__()

    def Total(self):
        # String que representa el monto total a transferir
        return self.combustible + self.viatico + self.hospedaje + self.peaje + self.imprevistos


class Registro(models.Model):

    # Modelo que contiene datos sobre los comprobantes de compras realizadas para la ejecucion de una tarea

    tarea = models.ForeignKey(Tarea, help_text="Seleccione tarea a la que esta asociada el comprobante",
                              on_delete=models.SET_NULL, null=True)
    nroComprobante = models.IntegerField(help_text="Ingrese el numero de comprobante")

    monto = models.IntegerField(help_text="Ingrese el monto de la compra en guaranies")

    TIPO = (
        ('c', 'Combustible'),
        ('v', 'Viatico'),
        ('p', 'Peaje'),
        ('i', 'Imprevistos'),
        ('h', 'Hospedaje')
    )
    tipo = models.CharField(max_length=1, choices=TIPO, help_text="Seleccione el tipo de producto adquirido",
                            default='c')

    razonSocial = models.CharField(max_length=30, help_text="Ingrese la Razon Social del emisor del comprobante")

    urlComprobante = models.CharField(max_length=200, help_text="URL de la imagen almacenada", blank=True)

    urlKilometraje = models.CharField(max_length=200, blank=True, null=True)

    urlDispenser = models.CharField(max_length=200, blank=True, null=True)

    RUC = models.IntegerField(help_text="Ingrese RUC del emisor del comprobante")

    VALIDADO = (
        ('s', 'Si'),
        ('n', 'No'),
    )

    validado = models.CharField(max_length=1, choices=VALIDADO, default='n')
    observacion = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        # String que representa a al Usuario
        return self.tarea.__str__()


class Reporte(models.Model):

    # Modelo que contiene datos de los reportes generados luego de la ejecucion de los trabajos

    fecha = models.DateField(auto_now=True)
    descripcion = models.TextField(max_length=1000, help_text="Ingrese una descripcion completa del trabajo realizado")
    tarea = models.ForeignKey(Tarea, help_text="Seleccione tarea a la que esta asociada el reporte",
                              on_delete=models.SET_NULL, null=True)
    costoCombustible = models.IntegerField(help_text="Ingrese el gasto utilizado en combustible para la "
                                                     "ejecucion de la tarea")
    costoPeaje = models.IntegerField(help_text="Ingrese el gasto utilizado en peajes para la ejecucion de la tarea")
    costoImprevistos = models.IntegerField(help_text="Ingrese el gasto utilizado en "
                                                     "imprevistos para la ejecucion de la tarea")

    observacion = models.TextField(max_length=1000, help_text="Observaciones", blank=True, null=True)

    def Tarea(self):
        # String que representa a al Usuario
        return self.tarea.__str__()

    def __str__(self):
        # String que representa a al Usuario
        return self.descripcion
