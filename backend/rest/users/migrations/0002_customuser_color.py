# Generated by Django 3.1 on 2020-11-19 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='color',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
