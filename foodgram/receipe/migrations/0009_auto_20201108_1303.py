# Generated by Django 3.0.11 on 2020-11-08 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipe', '0008_auto_20201108_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='value',
            field=models.IntegerField(default=1),
        ),
    ]
