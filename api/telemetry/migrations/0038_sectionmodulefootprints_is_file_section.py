# Generated by Django 4.1.1 on 2022-09-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0037_fieldsectionfootprints_name_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionmodulefootprints',
            name='is_file_section',
            field=models.BooleanField(default=False),
        ),
    ]