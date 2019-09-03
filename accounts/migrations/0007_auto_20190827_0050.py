# Generated by Django 2.1.5 on 2019-08-26 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190827_0035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='total_payments_made',
            new_name='propertys_payments_made',
        ),
        migrations.RenameField(
            model_name='property_payment',
            old_name='balance',
            new_name='total_balance',
        ),
        migrations.AlterField(
            model_name='buyer',
            name='property_bought',
            field=models.ManyToManyField(help_text='all properties bought by buyer', to='accounts.Property_id'),
        ),
        migrations.AlterField(
            model_name='property_payment',
            name='payment_expected',
            field=models.IntegerField(help_text='total payment expected from all properties bought', null=True),
        ),
    ]
