# Generated by Django 3.2.9 on 2021-11-13 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0007_auto_20211113_1905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_address',
            old_name='user_id',
            new_name='userid',
        ),
    ]
