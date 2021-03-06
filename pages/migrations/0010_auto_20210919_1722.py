# Generated by Django 3.2.7 on 2021-09-19 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20210919_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='phone',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Əsas ünvan'),
        ),
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.TextField(verbose_name='Ünvan'),
        ),
    ]
