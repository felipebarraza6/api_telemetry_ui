# Generated by Django 4.1 on 2022-08-18 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0017_webinars_img_present_alter_profilefootprints_file1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilefootprints',
            name='file1',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Inscripción de la empresa en el Registro respectivo con certificado de vigencia emitido dentro de los 60 días previos a la fecha de adhesión.'),
        ),
        migrations.AlterField(
            model_name='profilefootprints',
            name='file10',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Resoluciones de Calificación Ambiental de las instalaciones que se someterán al APL, en caso de que existan.'),
        ),
        migrations.AlterField(
            model_name='profilefootprints',
            name='file11',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Permisos o resoluciones sectoriales vigente de las instalaciones de r la empresa adherente en relación a los recursos hídricos.'),
        ),
        migrations.AlterField(
            model_name='profilefootprints',
            name='file12',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Declaracion Jurada'),
        ),
        migrations.AlterField(
            model_name='profilefootprints',
            name='file2',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Copia de la personería del representante legal, con certificado de vigencia emitido dentro de los 60 días previos a la fecha de adhesión, que lo habilita para firmar los documentos del APL.'),
        ),
        migrations.AlterField(
            model_name='profilefootprints',
            name='file3',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Copia del RUT de la Empresa.'),
        ),
        migrations.AlterField(
            model_name='profilefootprints',
            name='file4',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Copia de la patente municipal de la(s) instalación(es) que se someterá(n) al APL.'),
        ),
        migrations.AlterField(
            model_name='profilefootprints',
            name='file5',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Copia del título que lo habilita para usar el inmueble que se someterá al APL.'),
        ),
        migrations.AlterField(
            model_name='profilefootprints',
            name='file6',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Copia de la inscripción de dominio con vigencia dentro de los 60 días, de los Derechos de Agua en el Registro de Propiedad de Aguas respectivo.'),
        ),
        migrations.AlterField(
            model_name='profilefootprints',
            name='file7',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Certificado de inscripción de los derechos de agua en el Catastro Público de Aguas de la DGA, si correspondier, emitido dentro de los 60 dìas'),
        ),
        migrations.AlterField(
            model_name='profilefootprints',
            name='file8',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Certificado de pago de los derechos pecuniarios a la Asociación de Canalistas, si correspondiere.'),
        ),
        migrations.AlterField(
            model_name='profilefootprints',
            name='file9',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Título que faculta a la empresa adherente para hacer uso de las aguas, para el caso de que no tenga derechos de agua.'),
        ),
    ]
