# Generated by Django 2.1.5 on 2019-08-28 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('listings', '0003_auto_20190819_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='companies.Company'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor'),
        ),
    ]
