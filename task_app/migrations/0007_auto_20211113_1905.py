# Generated by Django 3.2.9 on 2021-11-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0006_auto_20211113_1854'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_new',
            options={'verbose_name_plural': 'user_new'},
        ),
        migrations.AlterField(
            model_name='user_new',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]