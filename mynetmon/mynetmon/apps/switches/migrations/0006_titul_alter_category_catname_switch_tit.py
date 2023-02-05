# Generated by Django 4.0.4 on 2022-05-17 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('switches', '0005_alter_category_catname_alter_switch_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Titul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titname', models.CharField(max_length=50, verbose_name='Титул')),
                ('titlocation', models.CharField(max_length=50, verbose_name='Зона №')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='catname',
            field=models.CharField(max_length=50, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='switch',
            name='tit',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.PROTECT, to='switches.titul', verbose_name='Титул'),
            preserve_default='True',
        ),
    ]