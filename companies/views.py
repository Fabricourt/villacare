from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .choices import company_name_choices,  town_choices 
from django.contrib.auth.models import User
from blog.models import Post
from .models import Company
from pages.models import Background_image

def companies(request):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    companys = Company.objects.order_by('-created_on').filter(is_published=True)

    paginator = Paginator(companys, 10)
    page = request.GET.get('page')
    paged_companys = paginator.get_page(page)    
    context = {
        'background_images':background_images,
        'companys':paged_companys,
        'posts':posts,
        'company_name_choices':company_name_choices,
        'town_choices': town_choices,
   
    }
    return render(request, 'companies/companies.html', context)



def company(request, rental_id):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    company = get_object_or_404(Companys, pk=company_id)
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    context = {
        'background_images':background_images,
        'company': company,
        'posts':posts,
    }
    return render(request, 'companies/company.html', context)


# Create your views here.
def companysearch(request):
  background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
  posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
  queryset_list = Company.objects.all().order_by('-created_on')
 
 



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

#Company name
  if 'company_name' in request.GET:
    company_name_choices = request.GET['company_name_choices']
    if company_name:
      queryset_list = queryset_list.filter(company_name__iexact=company_name_choices)



  context = {
        'background_images':background_images,
        'posts':posts,
        'company_name_choices': company_name_choices,
        'town_choices': town_choices,
        'companys': queryset_list,
        'values': request.GET

  }

  return  render(request, 'companies/companysearch.html', context)