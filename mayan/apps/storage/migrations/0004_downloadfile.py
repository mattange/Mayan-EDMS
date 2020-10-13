# Generated by Django 2.2.15 on 2020-10-13 11:48

from django.db import migrations, models
import django.db.models.deletion
import mayan.apps.storage.classes
import mayan.apps.storage.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('storage', '0003_auto_20200601_0649'),
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(storage=mayan.apps.storage.classes.DefinedStorageLazy(name='storage__downloadfile'), upload_to=mayan.apps.storage.models.download_file_upload_to, verbose_name='File')),
                ('filename', models.CharField(max_length=255, verbose_name='Filename')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Date time')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Download file',
                'verbose_name_plural': 'Download files',
            },
        ),
    ]