# Generated by Django 5.0.2 on 2024-02-27 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtapp', '0003_rename_ideas_idea'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='finance',
        ),
        migrations.RemoveField(
            model_name='user',
            name='idea',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pdp',
        ),
        migrations.RemoveField(
            model_name='user',
            name='personal',
        ),
    ]
