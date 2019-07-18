# Generated by Django 2.2.3 on 2019-07-10 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.UUIDField(default=uuid.uuid4, help_text='Identificador unico para el cliente', primary_key=True, serialize=False)),
                ('nombre', models.CharField(help_text='Ingrese el nombre del cliente', max_length=50)),
                ('rubro', models.CharField(help_text='Ingrese rubro en el que se desempena el cliente', max_length=50)),
                ('direccion', models.TextField(help_text='Ingrese la direccion del cliente', max_length=200)),
                ('contacto', phonenumber_field.modelfields.PhoneNumberField(help_text='Ingrese nro de contacto del Empleado', max_length=128, region=None)),
                ('observacion', models.TextField(help_text='Observaciones', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el nombre del proyecto', max_length=30)),
                ('tipo', models.CharField(help_text='Ingrese el tipo del trabajo a ejecutar', max_length=100)),
                ('observacion', models.TextField(help_text='Observaciones', max_length=1000, null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mgmtApp.Cliente')),
                ('encargado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
