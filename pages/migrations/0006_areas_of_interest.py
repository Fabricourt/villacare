# Generated by Django 2.1.5 on 2019-09-04 09:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_property_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Areas_of_interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.ImageField(blank=True, null=True, upload_to='links/%Y/%m/%d/')),
                ('link_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
