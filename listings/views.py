from django.shortcuts import render, get_object_or_404 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, plot_size_choices, location_choices, company_choices, town_choices
from django.http import HttpResponse
from .models import Snippet
from realtors.models import Realtor
from blog.models import Post
from pages.models import Background_image
from.models import Listing

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)
  posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
  background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]

  paginator = Paginator(listings, 12)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'background_images':'background_images',
    'posts':posts,
    'listings': paged_listings,
    'town_choices': town_choices,  
    'company_choices': company_choices,
    'location_choices': location_choices,
    'plot_size_choices': plot_size_choices,
    'price_choices': price_choices
 
    }
  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
  posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
  background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]

  context = {
    'background_images':'background_images',
    'posts':posts,
    'town_choices': town_choices,  
    'company_choices': company_choices,
    'location_choices': location_choices,
    'plot_size_choices': plot_size_choices,
    'price_choices': price_choices,
    'listing': listing
  }

  return render(request, 'listings/listing.html', context)

def search(request):
  background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
  posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
  queryset_list = Listing.objects.order_by('-list_date')

  #keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)


# Town
  if 'town' in request.GET:
    town = request.GET['town']
    if town:
      queryset_list = queryset_list.filter(town__iexact=town)


  # Location
  if 'company' in request.GET:
    company = request.GET['company']
    if company:
      queryset_list = queryset_list.filter(Company__iexact=company)
  

    # Location
  if 'location' in request.GET:
    location = request.GET['location']
    if location:
      queryset_list = queryset_list.filter(location__iexact=location)

 
  # plot_size
  if 'plot_size' in request.GET:
    plot_size = request.GET['plot_size']
    if plot_size:
      queryset_list = queryset_list.filter(plot_size__lte=plot_size)

  # price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
        'background_images':'background_images',
        'posts':posts,
        'town_choices': town_choices,
        'company_choices': company_choices,
        'location_choices': location_choices,
        'plot_size_choices': plot_size_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET

  }

  return  render(request, 'listings/search.html', context)

def snippet_detail(request, slug):
  snippet = get_object_or_404(Snippet, slug=slug)
  return HttpResponse(f'This should be the detail view for the slug of {slug}')
