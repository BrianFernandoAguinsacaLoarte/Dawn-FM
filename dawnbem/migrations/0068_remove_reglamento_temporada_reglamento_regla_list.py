# Generated by Django 4.2.3 on 2023-08-12 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0067_reglamento_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reglamento',
            name='Temporada',
        ),
        migrations.AddField(
            model_name='reglamento',
            name='regla_list',
            field=models.ManyToManyField(blank=True, default=None, related_name='reglamentos', to='dawnbem.regla'),
        ),
    ]
