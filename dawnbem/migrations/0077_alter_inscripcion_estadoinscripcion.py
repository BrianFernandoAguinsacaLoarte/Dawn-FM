# Generated by Django 4.2.3 on 2023-08-12 23:13

import dawnbem.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0076_alter_inscripcion_estadoinscripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='EstadoInscripcion',
            field=models.CharField(blank=True, choices=[('Registrado', 'Registrado'), ('En Proceso', 'En Proceso'), ('Anulada', 'Anulada')], default=dawnbem.models.EstadoInscripcion['EN_PROCESO'], max_length=10),
        ),
    ]