# Generated by Django 3.2.6 on 2021-08-22 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0004_alter_taskmodel_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='priority',
            field=models.IntegerField(default=-1),
        ),
    ]
