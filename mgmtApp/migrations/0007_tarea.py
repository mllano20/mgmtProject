# Generated by Django 2.2.3 on 2019-07-10 18:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mgmtApp', '0006_vehiculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('idTarea', models.UUIDField(default=uuid.uuid4, help_text='Indentificador unico de la Tarea', primary_key=True, serialize=False)),
                ('descripcion', models.TextField(help_text='Ingrese una beve descripcion de la tarea a ejecutar', max_length=200)),
                ('fechaIni', models.DateField(help_text='Ingrese la fecha de inicio de la ejecucion de la tarea')),
                ('fechaFin', models.DateField(help_text='Ingrese la fecha de finalizacion de la ejecucion de la tarea')),
                ('observacion', models.TextField(help_text='Observaciones', max_length=1000, null=True)),
                ('proyecto', models.ForeignKey(help_text='Seleccione el proyecto al cual esta asociada esta tarea', null=True, on_delete=django.db.models.deletion.SET_NULL, to='mgmtApp.Proyecto')),
                ('team', models.ForeignKey(help_text='Seleccione el team encargado de ejecutar la tarea', null=True, on_delete=django.db.models.deletion.SET_NULL, to='mgmtApp.Team')),
                ('vehiculo', models.ForeignKey(help_text='Seleccione el vehiculoutilizado para la tarea', null=True, on_delete=django.db.models.deletion.SET_NULL, to='mgmtApp.Vehiculo')),
            ],
        ),
    ]