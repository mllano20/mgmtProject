# Generated by Django 2.2.3 on 2019-07-10 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mgmtApp', '0008_auto_20190710_1901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='usuario',
            new_name='usuarios',
        ),
    ]