# Generated by Django 4.1 on 2022-09-07 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0034_answerticket_is_admin_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerticket',
            name='administrator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
