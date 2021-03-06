# Generated by Django 2.1 on 2018-08-20 16:07

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_vehicle_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='data_owner',
            field=models.CharField(choices=[('custom', 'Custom'), ('decodethis', 'Decode this')], max_length=255),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='year',
            field=models.CharField(max_length=255),
        ),
    ]
