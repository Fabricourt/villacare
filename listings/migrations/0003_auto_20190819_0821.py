# Generated by Django 2.1.5 on 2019-08-19 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_remove_listing_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='roads',
            field=models.CharField(help_text='the distance from the main road', max_length=100),
        ),
    ]
