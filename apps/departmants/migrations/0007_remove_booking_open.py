# Generated by Django 3.1.3 on 2020-12-01 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departmants', '0006_auto_20201201_0559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='open',
        ),
    ]