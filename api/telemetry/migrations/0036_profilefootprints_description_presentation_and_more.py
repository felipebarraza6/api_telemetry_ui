# Generated by Django 4.1 on 2022-09-08 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0035_alter_answerticket_administrator'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilefootprints',
            name='description_presentation',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profilefootprints',
            name='title_presentation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
