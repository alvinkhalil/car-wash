# Generated by Django 3.2.7 on 2021-09-22 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Göndərilmə tarixi'),
        ),
    ]