# Generated by Django 4.1.1 on 2022-09-29 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0041_modulefootprints_is_hidden'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulefootprints',
            name='is_captation_data',
            field=models.BooleanField(default=False),
        ),
    ]
