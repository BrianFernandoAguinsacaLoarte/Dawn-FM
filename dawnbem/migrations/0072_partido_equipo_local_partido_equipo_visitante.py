# Generated by Django 4.2.3 on 2023-08-12 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0071_remove_partido_equipo_local_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='equipo_local',
            field=models.CharField(default='Sin definir', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partido',
            name='equipo_visitante',
            field=models.CharField(default='Sin definir', max_length=50),
            preserve_default=False,
        ),
    ]
