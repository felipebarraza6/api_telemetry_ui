# Generated by Django 4.1.1 on 2022-09-29 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0040_modulefootprints_is_complete_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulefootprints',
            name='is_hidden',
            field=models.BooleanField(default=False),
        ),
    ]
