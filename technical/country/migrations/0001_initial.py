# Generated by Django 3.0.6 on 2020-05-11 17:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creación')),
                ('write_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de modificación')),
                ('version', models.IntegerField(default=1, verbose_name='Versión')),
                ('iso_alpha_code', models.CharField(max_length=2, verbose_name='Código Alfabético ISO')),
                ('iso_numeric_code', models.CharField(max_length=3, verbose_name='Código Numérico ISO')),
                ('name', models.CharField(max_length=27, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Paises',
            },
        ),
    ]
