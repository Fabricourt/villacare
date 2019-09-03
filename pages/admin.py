from django.contrib import admin

from .models import Property_link,Link, Background_image

admin.site.register(Link)
admin.site.register(Property_link)
admin.site.register(Background_image)