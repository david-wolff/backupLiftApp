# Generated by Django 4.2.4 on 2023-10-06 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MeuApp', '0010_alter_ride_departure_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]