# Generated by Django 4.2.7 on 2023-12-04 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServisModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(choices=[('analysis', 'analysis'), ('flasks', 'flasks'), ('ideas', 'ideas')], max_length=221)),
                ('profession', models.CharField(max_length=221)),
            ],
        ),
    ]
