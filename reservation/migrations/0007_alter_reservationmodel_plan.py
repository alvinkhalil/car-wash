# Generated by Django 3.2.7 on 2021-09-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_reservationmodel_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='plan',
            field=models.CharField(choices=[('True', 'Qəbul edilib'), ('False', 'Gözləmədə')], max_length=100),
        ),
    ]