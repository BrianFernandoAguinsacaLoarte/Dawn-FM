# Generated by Django 4.2.3 on 2023-07-30 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0043_remove_partido_grupo_partido_grupo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='grupo',
        ),
    ]
