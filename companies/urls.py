from django.urls import path

from . import views

urlpatterns = [
    path('', views.companies, name='companies'),
    path('<int:company_id>', views.company, name='company'),
    path('companysearch', views.companysearch, name='companysearch'),
  
    
]