# Generated by Django 4.2.3 on 2023-07-28 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='EleccionDeRol',
            new_name='Rol',
        ),
    ]