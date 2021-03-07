# Generated by Django 3.1.7 on 2021-03-07 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('hin', models.CharField(max_length=50)),
                ('current_hours', models.IntegerField()),
                ('service_interval', models.IntegerField()),
                ('next_service', models.DateField()),
            ],
        ),
    ]