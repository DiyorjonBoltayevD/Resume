# Generated by Django 4.2.7 on 2023-12-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0006_user_ourblog_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourblog',
            name='user',
        ),
        migrations.AddField(
            model_name='ourblog',
            name='chat',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
