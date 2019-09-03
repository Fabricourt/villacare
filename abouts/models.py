from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class About(models.Model):
    title  = models.CharField(max_length=120)
    image   = models.ImageField(upload_to='image/', blank=True, null=True)
    content = RichTextField(null=True, blank=True)
    reload = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title