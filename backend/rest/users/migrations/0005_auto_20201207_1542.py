# Generated by Django 3.1 on 2020-12-07 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201203_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Numero incorrecto', regex='^\\+?1?\\d{7,10}$')]),
        ),
    ]
