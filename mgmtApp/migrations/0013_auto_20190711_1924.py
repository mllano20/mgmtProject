# Generated by Django 2.2.3 on 2019-07-11 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mgmtApp', '0012_reporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='encargado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='encargado', to=settings.AUTH_USER_MODEL),
        ),
    ]