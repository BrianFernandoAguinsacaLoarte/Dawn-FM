# Generated by Django 4.2.3 on 2023-07-29 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0032_alter_registro_escogerdeporte'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='EscogerDeporte',
        ),
    ]
