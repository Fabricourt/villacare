# Generated by Django 2.1.5 on 2019-08-27 04:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0009_buyer_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='contact',
        ),
        migrations.AddField(
            model_name='buyer',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
