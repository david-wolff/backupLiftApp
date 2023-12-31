# Generated by Django 4.2.4 on 2023-09-29 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MeuApp', '0006_ride_free_seats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='passenger',
        ),
        migrations.AddField(
            model_name='ride',
            name='passengers',
            field=models.ManyToManyField(blank=True, related_name='rides_as_passenger', to='MeuApp.profile'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='departure_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='ride',
            name='free_seats',
            field=models.PositiveIntegerField(),
        ),
    ]
