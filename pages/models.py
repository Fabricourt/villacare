from django.db import models
from django.utils import timezone
from django.urls import reverse

#Property Links
class Property_link(models.Model):
    title = models.CharField(max_length=100)
    link_name = models.CharField(max_length=200)
    link_url = models.CharField(max_length=200, blank=False, null=True)
    link_pic = models.ImageField(upload_to='links/%Y/%m/%d/', null=True, blank=True)
    link_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



# construction Links
class Link(models.Model):
    title = models.CharField(max_length=100)
    link_name = models.CharField(max_length=200)
    link_url = models.CharField(max_length=200, blank=False, null=True)
    link_pic = models.ImageField(upload_to='links/%Y/%m/%d/', null=True, blank=True)
    link_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Background_image(models.Model):
    title = models.CharField(max_length=100)
    background_image = models.ImageField(upload_to='links/%Y/%m/%d/', null=True, blank=True)
    link_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title
