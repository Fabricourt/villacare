from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    testimonials_image = models.ImageField(default='default.jpg', upload_to='testimonials_images')
    message = RichTextField(max_length=999, blank=True, null=True)
    post_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user}'
    
    def save(self, **kwargs):
        super().save()
    
  