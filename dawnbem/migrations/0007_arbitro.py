# Generated by Django 4.2.3 on 2023-07-28 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0006_jugador_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arbitro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('numero_Colegiado', models.PositiveIntegerField()),
            ],
        ),
    ]
