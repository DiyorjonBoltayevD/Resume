# Generated by Django 4.2.7 on 2023-12-04 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0004_ourprojects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ourblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='ourblog/')),
                ('title', models.CharField(max_length=221)),
                ('content', models.CharField(max_length=221)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
