# Generated by Django 4.2.3 on 2023-07-29 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0025_alter_registro_escogerdeporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='otro',
            field=models.CharField(default='Valor_Predeterminado', max_length=50),
        ),
        migrations.AlterField(
            model_name='registro',
            name='EscogerDeporte',
            field=models.CharField(choices=[('Futbol', 'Futbol'), ('Basquet', 'Basquet'), ('Voley', 'Voley')], max_length=50),
        ),
    ]
