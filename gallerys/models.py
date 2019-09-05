from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from accounts .models import User
from PIL import Image

        
class Photo(models.Model):
  title  = models.CharField(max_length=120, blank=False, null=True)
  name = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  description = RichTextField(blank=True, null=True)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
  is_published = models.BooleanField(default=True)
  reload = models.DateTimeField(default=timezone.now)
  def __str__(self):
    return self.title