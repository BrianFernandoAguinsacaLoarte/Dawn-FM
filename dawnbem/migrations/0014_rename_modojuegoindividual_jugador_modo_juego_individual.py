# Generated by Django 4.2.3 on 2023-07-29 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0013_jugador'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jugador',
            old_name='ModoJuegoIndividual',
            new_name='Modo_Juego_Individual',
        ),
    ]
