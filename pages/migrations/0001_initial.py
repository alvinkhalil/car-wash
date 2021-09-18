# Generated by Django 3.2.7 on 2021-09-18 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coverimages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ad')),
                ('description', models.TextField(verbose_name='Məlumat')),
                ('image', models.ImageField(upload_to='sliders', verbose_name='Şəkil')),
                ('status', models.CharField(choices=[('active', 'Paylaşılıb'), ('draft', 'Qaralama')], max_length=100, verbose_name='Status')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]