# Generated by Django 4.2.3 on 2023-07-28 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0009_remove_jugador_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arbitro',
            name='nombre',
        ),
    ]