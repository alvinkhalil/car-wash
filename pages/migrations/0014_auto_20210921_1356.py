# Generated by Django 3.2.7 on 2021-09-21 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='text',
        ),
        migrations.AddField(
            model_name='price',
            name='pr1',
            field=models.CharField(blank=True, max_length=100, verbose_name='Paketə daxildir'),
        ),
        migrations.AddField(
            model_name='price',
            name='pr10',
            field=models.CharField(blank=True, max_length=100, verbose_name='Paketə daxildir'),
        ),
        migrations.AddField(
            model_name='price',
            name='pr2',
            field=models.CharField(blank=True, max_length=100, verbose_name='Paketə daxildir'),
        ),
        migrations.AddField(
            model_name='price',
            name='pr3',
            field=models.CharField(blank=True, max_length=100, verbose_name='Paketə daxildir'),
        ),
        migrations.AddField(
            model_name='price',
            name='pr4',
            field=models.CharField(blank=True, max_length=100, verbose_name='Paketə daxildir'),
        ),
        migrations.AddField(
            model_name='price',
            name='pr5',
            field=models.CharField(blank=True, max_length=100, verbose_name='Paketə daxildir'),
        ),
        migrations.AddField(
            model_name='price',
            name='pr6',
            field=models.CharField(blank=True, max_length=100, verbose_name='Paketə daxildir'),
        ),
        migrations.AddField(
            model_name='price',
            name='pr7',
            field=models.CharField(blank=True, max_length=100, verbose_name='Paketə daxildir'),
        ),
        migrations.AddField(
            model_name='price',
            name='pr8',
            field=models.CharField(blank=True, max_length=100, verbose_name='Paketə daxildir'),
        ),
        migrations.AddField(
            model_name='price',
            name='pr9',
            field=models.CharField(blank=True, max_length=100, verbose_name='Paketə daxildir'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.FloatField(verbose_name='Qiymət'),
        ),
    ]
