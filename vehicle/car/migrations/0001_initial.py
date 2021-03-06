# Generated by Django 3.1.7 on 2021-03-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('vin', models.CharField(max_length=50)),
                ('current_mileage', models.IntegerField()),
                ('service_interval', models.IntegerField()),
                ('next_service', models.DateField()),
            ],
        ),
    ]
