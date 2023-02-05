# Generated by Django 4.0.4 on 2022-05-16 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('switches', '0002_remove_switch_categ'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(default='Switch', max_length=50, verbose_name='Имя устройства')),
            ],
        ),
        migrations.AddField(
            model_name='switch',
            name='category',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='switches.category'),
            preserve_default='True',
        ),
    ]
