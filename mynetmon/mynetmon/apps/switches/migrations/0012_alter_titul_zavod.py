# Generated by Django 4.0.4 on 2022-06-10 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switches', '0011_category_catcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titul',
            name='zavod',
            field=models.CharField(default='1 Зона', max_length=50, verbose_name='Завод'),
        ),
    ]
