# Generated by Django 4.2 on 2023-04-19 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_carrito'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
    ]