# Generated by Django 3.2.7 on 2021-09-19 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20210919_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='facebook',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='location',
            name='instagram',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='location',
            name='linkedin',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='location',
            name='twitter',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='location',
            name='youtube',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='location',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='location',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Başlıq'),
        ),
    ]
