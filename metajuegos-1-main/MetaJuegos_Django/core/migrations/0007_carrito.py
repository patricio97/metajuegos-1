# Generated by Django 4.2 on 2023-04-19 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('idCarrito', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Carrito')),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
    ]