# Generated by Django 2.1.4 on 2018-12-12 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitbit_api', '0002_auto_20181212_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='test1',
            field=models.CharField(default='test', max_length=100),
        ),
        migrations.AddField(
            model_name='usertoken',
            name='test2',
            field=models.CharField(default='test', max_length=100),
        ),
    ]
