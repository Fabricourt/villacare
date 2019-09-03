from django.db import models
from datetime import datetime
from realtors.models import Realtor
from ckeditor.fields import RichTextField
from companies.models import Company
from django.utils.text import slugify


class Snippet(models.Model):
  title = models.CharField(max_length=200, blank=True, null=True)
  slug = models.SlugField(blank=True, null=True)
  body = models.TextField(blank=True, null=True)

  def save(self, *args, **kwargs):
    self.slug =slugify(self.title)
    super().save(*args, **kwargs)




class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING,  blank=True, null=True)
  company = models.ForeignKey(Company, on_delete=models.DO_NOTHING,  blank=True, null=True)
  title = models.CharField(max_length=200, blank=True, null=True)
  town = models.CharField(max_length=200, blank=True, null=True)
  location = models.CharField(max_length=100, blank=True, null=True, help_text='particular name of the area as known to the locals' )
  description = RichTextField(blank=True, null=True)
  price = models.IntegerField()
  payment_plan = models.CharField(max_length=200, help_text='mode of payment required')
  water = models.CharField(max_length=100, help_text='the distance from water pipe or source')
  roads = models.CharField(max_length=100, help_text='the distance from the main road')
  electricity = models.CharField(max_length=100, help_text='distance from the closest transformer')                      
  plot_type = models.CharField(max_length=100)
  plot_size = models.CharField(max_length=100)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(blank=True, null=True)
  def __str__(self):
    return self.title




