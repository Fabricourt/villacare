from django.shortcuts import render
from home.models import Footer, Topbar
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from home.models import Topbar, Footer, Head
from.models import Photo
from blog.models import Post

def index(request):
  photos = Photo.objects.order_by('-reload').filter(is_published=True)
  topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
  footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
  posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
  paginator = Paginator(photos, 6)
  page = request.GET.get('page')
  paged_photos = paginator.get_page(page)

  context = {
    'photos': paged_photos,
    'posts':posts,
    'topbars': topbars,

    'footers': footers,
  }

  return render(request, 'gallerys/photos.html', context)



def photo(request, photo_id):
  photo = get_object_or_404(Photo, pk=photo_id)
  topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
  footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
  posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
  context = {
    'photo': photo,
    'posts':posts,
    'topbars': topbars,

    'footers': footers,
    
  }


  return render(request, 'gallerys/photo.html', context)