from django.urls import path

from . import views

urlpatterns = [
    path('', views.houses, name='houses'),
    path('<int:house_id>', views.house, name='house'),
    path('searchus', views.searchus, name='searchus'),
  
    
]