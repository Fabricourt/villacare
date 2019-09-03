from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField
from django.utils import timezone

class Location(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)

    def __str__(self):
        return self.name

#property number or  name 
class Property_id(models.Model):
    property_id = models.CharField(max_length=200, null=True, blank=False,)
    property_price_tag = models.CharField(max_length=200, null=True, blank=False,)
    Location = models.ForeignKey(Location, on_delete= models.CASCADE, null=True, blank=False)
    is_published = models.BooleanField(default=True)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.property_id

class Buyer(models.Model):
    buyer = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=False)
    name = models.CharField(max_length=200, null=True, blank=False)
    property_bought = models.ManyToManyField(Property_id, help_text='all properties bought by buyer')
    is_published = models.BooleanField(default=True)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Payment(models.Model):
    buyer = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=False)
    property_bought = models.ManyToManyField(Property_id, help_text='Select your properties')
    property_bought = models.ManyToManyField(Property_id, help_text='all properties bought by buyer')
    amount_paid = models.CharField(max_length=200, null=True, blank=False)
    is_published = models.BooleanField(default=True)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.amount_paid
 

class Account(models.Model):
    buyer = models.ManyToManyField(Buyer, help_text='Select The Buyer')
    contact_person = models.OneToOneField(User, on_delete= models.CASCADE, null=True, blank=False)
    property_bought = models.ManyToManyField(Property_id, help_text='Select your properties')
    payment_expected = models.IntegerField(blank=False, null=True, help_text='total payment expected from all properties bought')
    deposit_paid = models.IntegerField(blank=True, null=True)
    payment_made = models.ManyToManyField(Payment, help_text='Select your payments made so far')
    total_payments = models.IntegerField(blank=False, null=True)
    total_balance = models.IntegerField(blank=False, null=True)
    is_published = models.BooleanField(default=True)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.contact_person.username} Account'

    def save(self, **kwargs):
        super().save()
 

 

 

 