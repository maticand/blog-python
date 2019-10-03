# Generated by Django 2.2.5 on 2019-10-03 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de Autor')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido de Autor')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
                ('estado', models.BooleanField(default=True, verbose_name='Activo/No Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la Categoría')),
                ('estado', models.BooleanField(default=True, verbose_name='Activo/No Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
    ]