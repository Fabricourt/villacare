from django.urls import path

from . import views

urlpatterns = [
    path('', views.fundis, name='fundis'),
    path('<int:fundi_id>', views.fundi, name='fundi'),
    path('searches', views.searches, name='searches'),
  
    
]