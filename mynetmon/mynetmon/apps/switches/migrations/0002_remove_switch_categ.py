# Generated by Django 4.0.4 on 2022-05-16 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('switches', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='switch',
            name='categ',
        ),
    ]
