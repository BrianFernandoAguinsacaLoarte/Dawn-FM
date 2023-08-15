# Generated by Django 4.2.3 on 2023-08-05 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0053_alter_jugador_posicion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='inscripcion',
        ),
        migrations.AddField(
            model_name='equipo',
            name='inscripcion',
            field=models.ManyToManyField(blank=True, related_name='equipos', to='dawnbem.inscripcion'),
        ),
    ]
