# Generated by Django 3.1.3 on 2020-11-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0002_auto_20201111_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tienda',
            name='nombre',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]