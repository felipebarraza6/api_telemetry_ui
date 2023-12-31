# Generated by Django 4.1 on 2022-09-07 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0033_ticketsupport_is_open_ticketsupport_is_resolved'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerticket',
            name='is_admin_answer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='answerticket',
            name='is_client_answer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ticketsupport',
            name='support_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.supportsection'),
        ),
    ]
