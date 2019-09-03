from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .choices import product_choices,  town_choices
from django.contrib.auth.models import User
from blog.models import Post
from .models import Hardware, Product
from pages.models import Background_image

def hardwares(request):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    hardwares = Hardware.objects.order_by('-created_on').filter(is_published=True)

    paginator = Paginator(hardwares, 10)
    page = request.GET.get('page')
    paged_hardwares = paginator.get_page(page)    
    context = {
        'background_images':background_images,
        'hardwares':paged_hardwares,
        'posts':posts,
        'product_choices':product_choices,
        'town_choices': town_choices,
       
 
    }
    return render(request, 'hardwares/hardwares.html', context)



def hardware(request, hardware_id):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    hardware = get_object_or_404(Hardware, pk=hardware_id)
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    context = {
        'background_images':background_images,
        'hardware': hardware,
        'posts':posts,
    }
    return render(request, 'hardwares/hardware.html', context)


# Create your views here.
def searchall(request):
  background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
  posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
  queryset_list = Hardware.objects.order_by('-created_on')
  #queryset_list = Product.objects.order_by('-created_on')
 
 

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



#  Product
  if 'product' in request.GET:
    product = request.GET['product']
    if product:
      queryset_list = queryset_list.filter(product__exact=product)


  # service charge
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
        'background_images':background_images,
        'posts':posts,
        'product_choices': product_choices,
        'town_choices': town_choices,
        'hardwares': queryset_list,
        #'products': queryset_list,
        'values': request.GET

  }

  return  render(request, 'hardwares/searchall.html', context)