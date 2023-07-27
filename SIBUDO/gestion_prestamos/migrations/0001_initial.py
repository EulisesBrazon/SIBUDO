# Generated by Django 4.2.1 on 2023-07-27 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_est', models.PositiveBigIntegerField()),
                ('tipo_recurso', models.IntegerField()),
                ('id_recurso', models.IntegerField()),
                ('fecha_prestamo', models.DateField()),
                ('fecha_devolucion', models.DateField()),
                ('estado_prestamo', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Prestamo',
                'verbose_name_plural': 'Prestamos',
            },
        ),
        migrations.CreateModel(
            name='Recurso_Disponible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_recurso', models.IntegerField()),
                ('tipo_recurso', models.IntegerField()),
                ('n_disponibles', models.PositiveBigIntegerField()),
                ('tipo_prestamo', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Recurso_Disponible',
                'verbose_name_plural': 'Recursos_Disponibles',
            },
        ),
        migrations.CreateModel(
            name='Sancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_prestamo', models.IntegerField()),
                ('estado', models.BooleanField()),
                ('fecha_aplicacion', models.DateField()),
                ('fecha_culminacion', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Sancion',
                'verbose_name_plural': 'Sanciones',
            },
        ),
    ]
