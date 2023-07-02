# Generated by Django 4.1.7 on 2023-02-27 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0049_variableclient_type_variable'),
    ]

    operations = [
        migrations.CreateModel(
            name='EconomicActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Fecha de modificacion.', verbose_name='modified at')),
                ('name', models.CharField(max_length=1200)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'abstract': False,
            },
        ),
    ]