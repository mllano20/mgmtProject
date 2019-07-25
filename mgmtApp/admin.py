from django.contrib import admin
from .models import Cliente, Proyecto, Team, Vehiculo, Tarea, Transaccion, Registro, Reporte, Sitio, reporteSitio
from .models import Imagen


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rubro', 'direccion', 'contacto')


class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cliente', 'encargado', 'tipo')


class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'nroPatente')
    list_filter = ('modelo', 'marca', 'nroPatente')


class TareaAdmin(admin.ModelAdmin):
    list_display = ('fechaIni', 'fechaFin', 'descripcion', 'vehiculo')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'display_users')


class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'fecha', 'nroTransaccion', 'combustible', 'viatico', 'hospedaje', 'peaje', 'imprevistos',
                    'Total')


class RegistroAdmin(admin.ModelAdmin):
    list_display = ('razonSocial', 'RUC', 'nroComprobante', 'monto', 'validado')
    fieldsets = (('Datos del Comerciante', {
        'fields': ['nroComprobante', ('razonSocial', 'RUC')]
    }), ('Datos de Compra', {
        'fields': ('tarea', 'tipo', 'monto', 'observacion')
    }))


class ReporteAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'descripcion', 'Tarea')


class SitioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'coordenadas')


admin.site.register(Team, TeamAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Tarea)
admin.site.register(Transaccion, TransaccionAdmin)
admin.site.register(Registro, RegistroAdmin)
admin.site.register(Reporte, ReporteAdmin)
admin.site.register(Sitio, SitioAdmin)
admin.site.register(reporteSitio)
admin.site.register(Imagen)

