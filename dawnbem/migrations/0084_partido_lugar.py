# Generated by Django 4.2.3 on 2023-08-13 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0083_alter_partido_equipo_local_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='lugar',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
