# Generated by Django 5.1.2 on 2024-11-23 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0009_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
    ]