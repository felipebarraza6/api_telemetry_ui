# Generated by Django 4.1.1 on 2022-09-29 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0042_modulefootprints_is_captation_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modulefootprints',
            name='is_captation_data',
        ),
        migrations.AddField(
            model_name='sectionmodulefootprints',
            name='is_captation_data',
            field=models.BooleanField(default=False),
        ),
    ]
