# Generated by Django 4.1 on 2022-08-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0018_alter_profilefootprints_file1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='webinars',
            name='wallpaper_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]