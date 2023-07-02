# Generated by Django 3.0.5 on 2020-07-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='note',
            field=models.TextField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='client',
            name='flow_rates',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='charge',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
    ]