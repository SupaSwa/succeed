# Generated by Django 3.2.12 on 2024-03-20 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supaswa1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='event_id',
            new_name='event_time',
        ),
    ]
