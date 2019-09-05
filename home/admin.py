from django.contrib import admin
from .models import Topbar, Head, Footer


admin.site.register(Footer)

class HeadAdmin(admin.ModelAdmin):
    list_display = ('title', 'logo_short_name', 'motivational_statement')
admin.site.register(Head, HeadAdmin)

class TopbarAdmin(admin.ModelAdmin):
    list_display = ('title', 'statement')
admin.site.register(Topbar, TopbarAdmin)