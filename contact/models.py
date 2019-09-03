from django.db import models
from datetime import datetime
from realtors.models import Realtor
from ckeditor.fields import RichTextField
from PIL import Image


# Create your models here.
class Contact(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email = models.EmailField()
    message = RichTextField()
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='contact_pics')

        

    def __str__(self):
     return f'{self.first_name}  {self.last_name}  {self.contact_date}'
     
    def save(self, **kwargs):
        super().save()



class Sema(models.Model):
  listing = models.CharField(max_length=200)
  listing_id = models.IntegerField()
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)
  def __str__(self):
    return self.name

