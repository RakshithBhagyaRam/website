# Generated by Django 4.0.1 on 2022-01-23 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_phonenumber'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]