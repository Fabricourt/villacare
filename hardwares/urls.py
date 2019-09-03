from django.urls import path

from . import views

urlpatterns = [
    path('', views.hardwares, name='hardwares'),
    path('<int:hardware_id>', views.hardware, name='hardware'),
    path('searchall', views.searchall, name='searchall'),
  
    
]