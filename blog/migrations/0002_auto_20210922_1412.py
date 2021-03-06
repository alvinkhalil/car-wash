# Generated by Django 3.2.7 on 2021-09-22 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma tarixi'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='text',
            field=models.TextField(verbose_name='Mətin'),
        ),
    ]
