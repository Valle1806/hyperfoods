# Generated by Django 3.1 on 2020-10-13 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='credit_card',
            field=models.CharField(default=123654789654123, max_length=16),
            preserve_default=False,
        ),
    ]
