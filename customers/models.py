from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Customers(models.Model):
    title  = models.CharField(max_length=120)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    plot_number = models.CharField(max_length=200, blank=True, null=True)
    agreed_buying_price = models.CharField(max_length=200, blank=True, null=True)
    deposit = models.CharField(max_length=200, blank=True, null=True)
    
    content = RichTextField(null=True, blank=True)
    reload = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title