# Generated by Django 4.1.5 on 2023-01-21 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_foods_type_alter_activities_time_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='time_duration',
            field=models.IntegerField(),
        ),
    ]
