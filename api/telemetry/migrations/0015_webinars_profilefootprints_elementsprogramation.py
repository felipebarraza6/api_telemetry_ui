# Generated by Django 4.1 on 2022-08-18 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_alter_profileclient_scale_alter_quotation_client_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webinars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Fecha de modificacion.', verbose_name='modified at')),
                ('title', models.CharField(blank=True, max_length=355, null=True)),
                ('subtitule', models.CharField(blank=True, max_length=655, null=True)),
                ('organized_by', models.CharField(blank=True, max_length=655, null=True)),
                ('present', models.CharField(blank=True, max_length=655, null=True)),
                ('date_time_webinar', models.DateTimeField()),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProfileFootprints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Fecha de modificacion.', verbose_name='modified at')),
                ('economic_activity', models.CharField(blank=True, max_length=500, null=True)),
                ('res_1238', models.BooleanField(default=False)),
                ('size_company', models.CharField(blank=True, max_length=500, null=True)),
                ('name_represent_legal', models.CharField(blank=True, max_length=1200, null=True)),
                ('phone_represent_legal', models.CharField(blank=True, max_length=300, null=True)),
                ('mail_represent_legal', models.CharField(blank=True, max_length=500, null=True)),
                ('name_admin_apl_enterprise', models.CharField(blank=True, max_length=500, null=True)),
                ('phone_admin_apl_enterprise', models.CharField(blank=True, max_length=500, null=True)),
                ('mail_admin_apl_enterprise', models.CharField(blank=True, max_length=500, null=True)),
                ('activities_org_extraterritorial', models.CharField(blank=True, max_length=1500, null=True)),
                ('cert_postulation', models.CharField(blank=True, max_length=500, null=True)),
                ('file1', models.FileField(upload_to='')),
                ('file2', models.FileField(upload_to='')),
                ('file3', models.FileField(upload_to='')),
                ('file4', models.FileField(upload_to='')),
                ('file5', models.FileField(upload_to='')),
                ('file6', models.FileField(upload_to='')),
                ('file7', models.FileField(upload_to='')),
                ('file8', models.FileField(upload_to='')),
                ('file9', models.FileField(upload_to='')),
                ('file10', models.FileField(upload_to='')),
                ('file11', models.FileField(upload_to='')),
                ('file12', models.FileField(upload_to='')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.client')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElementsProgramation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Fecha de modificacion.', verbose_name='modified at')),
                ('prefix', models.CharField(max_length=10)),
                ('name', models.CharField(blank=True, max_length=655, null=True)),
                ('webinar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.webinars')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'abstract': False,
            },
        ),
    ]
