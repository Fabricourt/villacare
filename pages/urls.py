from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('lamu', views.lamu, name='lamu'),
    path('comingsoon', views.comingsoon, name='comingsoon'),
    path('mobile', views.mobile, name='mobile'), 
    path('tablet', views.tablet, name='tablet'),
    path('laptop', views.laptop, name='laptop'),
]

