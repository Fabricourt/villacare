from django.contrib import admin

# Register your models here.
from .models import House, Bedroom, Type_of_house, Bathroom

admin.site.register(Type_of_house)
admin.site.register(House)
admin.site.register(Bedroom)
admin.site.register(Bathroom)