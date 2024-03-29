# Generated by Django 2.1.5 on 2019-08-21 15:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link_name', models.CharField(max_length=200)),
                ('link_pic', models.ImageField(blank=True, null=True, upload_to='links/%Y/%m/%d/')),
                ('link_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
