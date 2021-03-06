# Generated by Django 2.1.5 on 2019-08-28 16:56

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('town', models.CharField(blank=True, max_length=200, null=True)),
                ('exact_location_name', models.CharField(blank=True, max_length=200, null=True)),
                ('about_company', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone1', models.CharField(blank=True, max_length=100, null=True)),
                ('phone2', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('youtube', models.CharField(blank=True, max_length=100, null=True)),
                ('photo_main', models.ImageField(upload_to='company_photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='company_photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='company_photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='company_photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='company_photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='company_photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='company_photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('contact_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
