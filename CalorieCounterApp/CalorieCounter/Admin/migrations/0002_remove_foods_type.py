# Generated by Django 4.1.5 on 2023-01-21 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foods',
            name='type',
        ),
    ]