# Generated by Django 3.2.7 on 2021-09-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationmodel',
            name='message',
            field=models.TextField(default=1, verbose_name='Mesaj'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservationmodel',
            name='status',
            field=models.CharField(choices=[('True', 'Qəbul edilib'), ('False', 'Gözləmədə')], max_length=100, verbose_name='Status'),
        ),
    ]
