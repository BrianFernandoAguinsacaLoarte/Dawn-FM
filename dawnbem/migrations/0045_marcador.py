# Generated by Django 4.2.3 on 2023-07-30 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0044_remove_equipo_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marcador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_equipo_local', models.CharField(max_length=50)),
                ('nombre_equipo_visitante', models.CharField(max_length=50)),
                ('punto_marcador_local', models.PositiveIntegerField()),
                ('punto_marcador_visitante', models.PositiveIntegerField()),
            ],
        ),
    ]
