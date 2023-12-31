# Generated by Django 4.1.2 on 2022-10-18 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0044_modulefootprints_is_blocked'),
    ]

    operations = [
        migrations.AddField(
            model_name='well',
            name='exact_address',
            field=models.TextField(blank=True, max_length=1200, null=True),
        ),
        migrations.AddField(
            model_name='well',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='well',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
