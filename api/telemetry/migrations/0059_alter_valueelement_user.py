# Generated by Django 4.2.1 on 2023-06-01 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0058_valueelement_code_alter_valueelement_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valueelement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
