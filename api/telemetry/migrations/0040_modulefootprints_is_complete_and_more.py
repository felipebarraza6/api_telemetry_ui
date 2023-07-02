# Generated by Django 4.1.1 on 2022-09-29 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0039_profileclient_code_dga_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulefootprints',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fieldsectionfootprints',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='fingerprint/annex/'),
        ),
        migrations.AlterField(
            model_name='webinars',
            name='img_present',
            field=models.ImageField(blank=True, null=True, upload_to='webinars/presents/'),
        ),
        migrations.AlterField(
            model_name='webinars',
            name='wallpaper_img',
            field=models.ImageField(blank=True, null=True, upload_to='webinars/wallpapers/'),
        ),
    ]
