# Generated by Django 4.2.3 on 2023-08-10 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0056_sorteo_fecha_sorteo_hora'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='grupoList',
            field=models.ManyToManyField(blank=True, related_name='equipos', to='dawnbem.grupo'),
        ),
    ]
