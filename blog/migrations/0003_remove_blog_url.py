# Generated by Django 3.1.1 on 2020-09-30 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200930_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='url',
        ),
    ]
