# Generated by Django 2.1 on 2022-01-08 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220108_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='phone_number',
            field=models.CharField(default='+91', max_length=10),
        ),
    ]
