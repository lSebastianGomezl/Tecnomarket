# Generated by Django 4.0.6 on 2022-08-09 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consultas', models.IntegerField()),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
    ]
