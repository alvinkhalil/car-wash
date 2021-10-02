# Generated by Django 3.2.7 on 2021-10-02 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210922_2115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogmodel',
            options={'verbose_name': 'Məqalə', 'verbose_name_plural': 'Məqalələr'},
        ),
        migrations.CreateModel(
            name='BlogLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogmodel')),
            ],
        ),
    ]
