# Generated by Django 2.1.5 on 2019-08-21 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_link_link_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
