from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User





class Company(models.Model):
    contact_person = models.ForeignKey(User, on_delete= models.CASCADE)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    town = models.CharField(max_length=200, blank=True, null=True)
    exact_location_name = models.CharField(max_length=200, blank=True, null=True)
    about_company = RichTextField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone1 = models.CharField(max_length=100, blank=True, null=True)
    phone2 = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    youtube = models.CharField(max_length=100, blank=True, null=True)
    photo_main = models.ImageField(upload_to='company_photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='company_photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='company_photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='company_photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='company_photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='company_photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='company_photos/%Y/%m/%d/', blank=True)    
    is_published = models.BooleanField(default=True)
    created_on = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.company_name



    
        