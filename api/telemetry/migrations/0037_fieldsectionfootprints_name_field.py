# Generated by Django 4.1.1 on 2022-09-12 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0036_profilefootprints_description_presentation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldsectionfootprints',
            name='name_field',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]