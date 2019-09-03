from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .choices import skill_choices, service_charge_choices,  town_choices
from django.contrib.auth.models import User
from .models import Fundi, Category
from blog.models import Post
from pages.models import Background_image


def fundis(request):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    fundis = Fundi.objects.order_by('-created_on').filter(is_published=True)

    paginator = Paginator(fundis, 10)
    page = request.GET.get('page')
    paged_fundis = paginator.get_page(page)    
    context = {
        'background_images':'background_images',
        'fundis':paged_fundis,
        'posts':posts,
        'town_choices': town_choices,
        'service_charge_choices': service_charge_choices,
        'skill_choices': skill_choices,
      
       
    }
    return render(request, 'fundis/fundis.html', context)



def fundi(request, fundi_id):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    fundi = get_object_or_404(Fundi, pk=fundi_id)
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    context = {
        'background_images':'background_images',
        'fundi': fundi,
        'posts':posts,
    }
    return render(request, 'fundis/fundi.html', context)

def searches(request):
  background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
  posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
  queryset_list = Fundi.objects.order_by('-created_on')

  #keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(resume__icontains=keywords)


# Town
  if 'town' in request.GET:
    town = request.GET['town']
    if town:
      queryset_list = queryset_list.filter(town__iexact=town)

  # skill
  if 'skill' in request.GET:
    skill = request.GET['skill']
    if skill:
      queryset_list = queryset_list.filter(skill__iexact=skill)

  # service charge
  if 'service_charge' in request.GET:
    service_charge = request.GET['service_charge']
    if service_charge:
      queryset_list = queryset_list.filter(service_charge__lte=service_charge)

  context = {
        'background_images':'background_images',
        'posts':posts,
        'town_choices': town_choices,
        'service_charge_choices': service_charge_choices,
        'skill_choices': skill_choices,
        'fundis': queryset_list,
        'values': request.GET

  }

  return  render(request, 'fundis/searches.html', context)

