# Generated by Django 4.2.3 on 2023-08-14 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dawnbem', '0086_delete_revisioninscripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCalendario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='partido',
            name='grupo',
        ),
        migrations.RemoveField(
            model_name='partido',
            name='lugar',
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('calendario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dawnbem.calendario')),
            ],
        ),
        migrations.AddField(
            model_name='calendario',
            name='tipo_calendario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dawnbem.tipocalendario'),
        ),
    ]
