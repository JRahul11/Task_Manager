# Generated by Django 3.2.6 on 2021-08-15 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0002_alter_taskmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
