# Generated by Django 4.1 on 2022-09-05 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0030_supportsection_alter_fieldsectionfootprints_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketsupport',
            name='footprint',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.profilefootprints'),
        ),
    ]
