# Generated by Django 2.1.5 on 2019-08-27 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20190827_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='contact',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
