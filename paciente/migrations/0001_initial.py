# Generated by Django 2.2.24 on 2021-11-14 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('rut', models.IntegerField(max_length=9, primary_key=True, serialize=False)),
                ('Nombres', models.CharField(max_length=30, verbose_name='Nombres del paciente')),
                ('Apellidos', models.CharField(max_length=45, verbose_name='Apellidos del paciente')),
                ('Direccion', models.CharField(max_length=200, verbose_name='Direccion del paciente')),
                ('nombreMedico', models.CharField(max_length=200, verbose_name='Nombre del medico')),
                ('FechaIngreso', models.DateField(auto_now_add=True, verbose_name='Fecha de ingreso')),
            ],
        ),
    ]
