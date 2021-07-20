# Generated by Django 2.2.3 on 2020-07-16 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conexion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Conexion',
                'verbose_name_plural': 'Conexiones',
                'ordering': ['tipo_conexion'],
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_departamento', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proveedor', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Conexion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_conexion', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Problema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_problema', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dui', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=9)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['dui'],
            },
        ),
        migrations.CreateModel(
            name='Velocidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_velocidad', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Problema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('conexion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crearReportes.Conexion')),
                ('tipo_problema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crearReportes.Tipo_Problema')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crearReportes.Usuario')),
            ],
            options={
                'verbose_name': 'Problema',
                'verbose_name_plural': 'Problemas',
                'ordering': ['conexion'],
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_municipio', models.CharField(max_length=60)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crearReportes.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crearReportes.Departamento')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crearReportes.Municipio')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crearReportes.Usuario')),
            ],
            options={
                'verbose_name': 'Direccion',
                'verbose_name_plural': 'Direcciones',
                'ordering': ['usuario'],
            },
        ),
        migrations.AddField(
            model_name='conexion',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crearReportes.Proveedor'),
        ),
        migrations.AddField(
            model_name='conexion',
            name='tipo_conexion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crearReportes.Tipo_Conexion'),
        ),
        migrations.AddField(
            model_name='conexion',
            name='velocidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crearReportes.Velocidad'),
        ),
    ]
