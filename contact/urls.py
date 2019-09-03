from django.urls import path

from . import views

urlpatterns = [
  path('sema', views.sema, name='sema'),
 
]
