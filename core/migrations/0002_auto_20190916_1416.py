# Generated by Django 2.2.5 on 2019-09-16 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='category',
            new_name='categories',
        ),
    ]
