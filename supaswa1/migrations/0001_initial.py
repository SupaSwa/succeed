# Generated by Django 3.2.12 on 2024-03-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_data', models.CharField(max_length=1000)),
                ('service_id', models.CharField(max_length=100)),
                ('event_id', models.CharField(max_length=100)),
                ('device_id', models.CharField(max_length=100)),
                ('Temperature_value', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
