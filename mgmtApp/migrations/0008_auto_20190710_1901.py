# Generated by Django 2.2.3 on 2019-07-10 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgmtApp', '0007_tarea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='observacion',
            field=models.TextField(blank=True, help_text='Observaciones', max_length=1000, null=True),
        ),
    ]