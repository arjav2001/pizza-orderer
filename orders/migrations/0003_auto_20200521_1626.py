# Generated by Django 2.1.7 on 2020-05-21 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200521_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
