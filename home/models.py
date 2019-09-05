from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Topbar(models.Model):
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    title = models.CharField(max_length=100)
    statement = RichTextField(blank=True, null=True)
    reload = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
        
class Head(models.Model):
    title = models.CharField(max_length=100)
    home_header = models.ImageField(upload_to='home_header/', blank=True, null=True)
    home_header_1 = models.ImageField(upload_to='home_header/', blank=True, null=True)
    home_header_2 = models.ImageField(upload_to='home_header/', blank=True, null=True)
    home_header_3 = models.ImageField(upload_to='home_header/', blank=True, null=True)
    logo_short_name = models.CharField(max_length=20, blank=True, null=True)
    motivational_statement = models.CharField(max_length=200, blank=True, null=True)
    reload = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Footer(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone1 = models.CharField(max_length=100, blank=True, null=True)
    phone2 = models.CharField(max_length=100, blank=True, null=True)
    description = RichTextField(blank=True, null=True)    
    email = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    youtube = models.CharField(max_length=100, blank=True, null=True)
    reload = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
