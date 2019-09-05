from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .choices import price_choices,  town_choices, bedroom_choices
from home.models import Topbar, Head, Footer
from django.contrib.auth.models import User
from blog.models import Post
from .models import House, Bedroom, Bathroom, Type_of_house
from pages.models import Background_image, Areas_of_interest

def houses(request):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    areas_of_interests = Areas_of_interest.objects.order_by('link_date').filter(is_published=True)[:1]
    heads = Head.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    houses = House.objects.order_by('-created_on').filter(is_published=True)

    paginator = Paginator(houses, 10)
    page = request.GET.get('page')
    paged_houses = paginator.get_page(page)    
    context = {
        'background_images':background_images,
        'areas_of_interests': areas_of_interests,
        'houses':paged_houses,
        'posts':posts,
        'topbars': topbars,
        'heads': heads,
        'footers': footers,
        'bedroom_choices':bedroom_choices,
        'town_choices': town_choices,
        'price_choices': price_choices,
 
    }
    return render(request, 'houses/houses.html', context)



def house(request, house_id):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    house = get_object_or_404(House, pk=house_id)
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    heads = Head.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    context = {
        'background_images':background_images,
        'house': house,
        'posts':posts,
        'topbars': topbars,
        'heads': heads,
        'footers': footers,
    }
    return render(request, 'houses/house.html', context)


# Create your views here.
def searchus(request):
  background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
  posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
  topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
  heads = Head.objects.order_by('-reload').filter(is_published=True)[:1]
  footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
  queryset_list = House.objects.all().order_by('-created_on')
 
 

  #keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(about_me__icontains=keywords)


#keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(name__icontains=keywords)
     


# Town
  if 'town' in request.GET:
    town = request.GET['town']
    if town:
      queryset_list = queryset_list.filter(town__iexact=town)

#  House
  if 'bedroom' in request.GET:
    bedroom = request.GET['bedroom']
    if bedroom:
      queryset_list = queryset_list.filter(bedroom__lte=bedroom)



  # service charge
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
        'background_images':background_images,
        'posts':posts,
        'topbars': topbars,
        'heads': heads,
        'footers': footers,
        'bedroom_choices': bedroom_choices,
        'town_choices': town_choices,
        'price_choices': price_choices,
        'houses': queryset_list,
        'values': request.GET

  }

  return  render(request, 'houses/searchus.html', context)