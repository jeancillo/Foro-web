# Generated by Django 3.0.8 on 2020-07-26 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30, unique=True)),
                ('dni', models.CharField(max_length=8, unique=True)),
                ('FechaNacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('Sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1)),
                ('usuario', models.CharField(max_length=20, unique=True)),
                ('clave', models.CharField(max_length=20)),
            ],
        ),
    ]
