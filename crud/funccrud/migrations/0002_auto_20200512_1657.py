# Generated by Django 3.0.5 on 2020-05-12 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funccrud', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='Post',
        ),
    ]
