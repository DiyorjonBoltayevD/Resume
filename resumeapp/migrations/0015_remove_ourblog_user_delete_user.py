# Generated by Django 4.2.7 on 2023-12-05 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0014_user_ourblog_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourblog',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]