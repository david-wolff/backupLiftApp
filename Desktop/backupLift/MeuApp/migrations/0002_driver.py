# Generated by Django 4.2.4 on 2023-09-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MeuApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter the driver name', max_length=100)),
                ('age', models.IntegerField(help_text='Enter the age')),
                ('email', models.EmailField(help_text='Enter the email', max_length=254)),
                ('phone', models.CharField(help_text='Phone with country and area code', max_length=20)),
                ('vehicle_model', models.CharField(help_text='Enter the vehicle model', max_length=100)),
                ('vehicle_number', models.CharField(help_text='Enter the vehicle number', max_length=20)),
                ('available_seats', models.IntegerField(help_text='Enter the number of available seats')),
                ('destination', models.CharField(help_text='Enter the destination', max_length=100)),
                ('departure_time', models.DateTimeField(help_text='Enter the departure time')),
                ('is_available', models.BooleanField(default=True, help_text='Is the driver available for a ride?')),
            ],
        ),
    ]
