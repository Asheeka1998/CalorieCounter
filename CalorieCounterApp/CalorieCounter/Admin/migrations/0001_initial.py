# Generated by Django 4.1.5 on 2023-01-21 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_name', models.CharField(max_length=200)),
                ('time_duration', models.TimeField()),
                ('calorie_burns', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('calories', models.FloatField(default=0)),
            ],
        ),
    ]
