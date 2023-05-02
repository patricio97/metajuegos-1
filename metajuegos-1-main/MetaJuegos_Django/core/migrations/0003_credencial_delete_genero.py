# Generated by Django 4.2 on 2023-04-17 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_genero_delete_credencial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credencial',
            fields=[
                ('idUsuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Usuario')),
                ('nombreUsuario', models.CharField(max_length=60, verbose_name='Nombre de Usuario')),
            ],
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
    ]