from django.urls import path

from . import views

urlpatterns = [
    path('', views.rentals, name='rentals'),
    path('<int:rental_id>', views.rental, name='rental'),
    path('searchrentals', views.searchrentals, name='searchrentals'),
  
    
]