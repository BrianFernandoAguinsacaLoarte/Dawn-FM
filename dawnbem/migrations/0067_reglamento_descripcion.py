# Generated by Django 4.2.3 on 2023-08-12 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0066_regla_nombre_regla_alter_regla_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='reglamento',
            name='descripcion',
            field=models.CharField(default='Sin descripcion', max_length=50),
            preserve_default=False,
        ),
    ]
