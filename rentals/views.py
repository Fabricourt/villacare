from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .choices import price_choices,  town_choices, bedroom_choices, bathroom_choices, type_of_house_choices
from django.contrib.auth.models import User
from blog.models import Post
from .models import Rental, Bedroom, Type_of_house, Bathroom
from pages.models import Background_image, Areas_of_interest
from home.models import Topbar, Footer, Head

def rentals(request):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    rentals = Rental.objects.order_by('-created_on').filter(is_published=True)
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    heads = Head.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    areas_of_interests = Areas_of_interest.objects.order_by('link_date').filter(is_published=True)[:1]

    paginator = Paginator(rentals, 10)
    page = request.GET.get('page')
    paged_rentals = paginator.get_page(page)    
    context = {
        'background_images':background_images,
        'topbars': topbars,
        'heads': heads,
        'footers': footers, 
        'rentals':paged_rentals,
        'posts':posts,
        'bedroom_choices':bedroom_choices,
        'bathroom_choices':bathroom_choices,
        'type_of_house_choices':type_of_house_choices,
        'town_choices': town_choices,
        'price_choices': price_choices,
 
    }
    return render(request, 'rentals/rentals.html', context)



def rental(request, rental_id):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    rental = get_object_or_404(Rental, pk=rental_id)
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    heads = Head.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    context = {
        'background_images':background_images,
        'rental': rental,
        'posts':posts,
        'topbars': topbars,
        'heads': heads,
        'footers': footers, 
    }
    return render(request, 'rentals/rental.html', context)


# Create your views here.
def searchrentals(request):
  background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
  posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
  topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
  heads = Head.objects.order_by('-reload').filter(is_published=True)[:1]
  footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
  queryset_list = Rental.objects.all().order_by('-created_on')
 
 

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

#type_of_house_choices
  if 'type_of_house_choices' in request.GET:
    type_of_house_choices = request.GET['type_of_house_choices']
    if type_of_house_choices:
      queryset_list = queryset_list.filter(town__iexact=type_of_house_choices)

#  Bedroom
  if 'bedroom' in request.GET:
    bedroom = request.GET['bedroom']
    if bedroom:
      queryset_list = queryset_list.filter(bedroom__lte=bedroom)

#  Bathroom
  if 'bathroom' in request.GET:
    bathromm = request.GET['bathroom']
    if bathroom:
      queryset_list = queryset_list.filter(bathroom__lte=bathroom)


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
        'bathroom_choices': bathroom_choices,
        'type_of_house_choices': type_of_house_choices,
        'town_choices': town_choices,
        'price_choices': price_choices,
        'rentals': queryset_list,
        'values': request.GET

  }

  return  render(request, 'rentals/searchrentals.html', context)