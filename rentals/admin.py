from django.contrib import admin

# Register your models here.
from .models import Rental, Bedroom, Type_of_house, Bathroom

admin.site.register(Type_of_house)
admin.site.register(Rental)
admin.site.register(Bedroom)
admin.site.register(Bathroom)