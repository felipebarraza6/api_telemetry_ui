# Generated by Django 4.1 on 2022-08-30 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0026_optionsselectionfieldfootprints'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldsectionfootprints',
            name='value',
            field=models.CharField(blank=True, max_length=1800, null=True),
        ),
    ]