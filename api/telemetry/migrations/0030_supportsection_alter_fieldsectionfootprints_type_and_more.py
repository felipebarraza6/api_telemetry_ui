# Generated by Django 4.1 on 2022-09-05 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0029_profilefootprints_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Fecha de modificacion.', verbose_name='modified at')),
                ('name', models.CharField(max_length=350)),
                ('description', models.TextField(blank=True, max_length=1200, null=True)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='fieldsectionfootprints',
            name='type',
            field=models.CharField(choices=[('SELECT', 'SELECT'), ('FILE', 'FILE'), ('TEXT', 'TEXT')], max_length=500),
        ),
        migrations.CreateModel(
            name='TicketSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Fecha de modificacion.', verbose_name='modified at')),
                ('affair', models.TextField(max_length=1200)),
                ('support_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.supportsection')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnswerTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Fecha de modificacion.', verbose_name='modified at')),
                ('answer', models.TextField(max_length=1200)),
                ('administrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ticket_support', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ticketsupport')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'abstract': False,
            },
        ),
    ]
