# Generated by Django 3.1.3 on 2020-12-03 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departmants', '0003_auto_20201203_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='phone_of_department',
        ),
    ]
