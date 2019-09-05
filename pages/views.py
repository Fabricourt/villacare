from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, plot_size_choices, location_choices, town_choices
from django.contrib.admin.views.decorators import staff_member_required
from testimonials.models import Testimonial
from listings.models import Listing
from realtors.models import Realtor
from blog.models import Post
from abouts.models import About
from home.models import Topbar, Head, Footer
from pages.models import Property_link, Link, Background_image, Areas_of_interest


from django.contrib.auth.decorators import login_required


def index(request):
    abouts = About.objects.order_by('-reload').filter(is_published=True)[:1]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    areas_of_interests = Areas_of_interest.objects.order_by('link_date').filter(is_published=True)[:1]
    heads = Head.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:6]
    testimonials = Testimonial.objects.order_by('-post_date').filter(is_published=True)[:3]
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]

    #property links
    property_links =Property_link.objects.order_by('link_date').filter(is_published=True)

    #construction link
    links = Link.objects.order_by('link_date').filter(is_published=True)
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]

    context = {
        'abouts': abouts,
        'areas_of_interests': areas_of_interests,
        'topbars': topbars,
        'heads': heads,
        'footers': footers,
        'background_images': background_images,
        'property_links':property_links,
        'links': links,
        'posts': posts,
        'listings': listings,
        'town_choices': town_choices,  
        'location_choices': location_choices,
        'plot_size_choices': plot_size_choices,
        'price_choices': price_choices,
        'testimonials': testimonials,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    heads = Head.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]

    context = {
        'topbars': topbars,
        'heads': heads,
        'footers': footers,
        'posts':posts,
        'background_images':'background_images',        
        'realtors': realtors,
        'town_choices': town_choices,  
        'location_choices': location_choices,
        'plot_size_choices': plot_size_choices,
        'price_choices': price_choices,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)

def lamu(request):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    heads = Head.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]

    context = {
        'background_images':'background_images',        
        'posts':posts,
        'topbars': topbars,
        'heads': heads,
        'footers': footers,
    }
    return render(request, 'pages/lamu.html', context)

def comingsoon(request):
    background_images = Background_image.objects.order_by('link_date').filter(is_published=True)[:1]
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    heads = Head.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    context = {
        'background_images':'background_images',
        'posts':posts,
        'topbars': topbars,
        'heads': heads,
        'footers': footers,
    }
    return render(request, 'pages/comingsoon.html', context)

@staff_member_required
def mobile(request):
    return render(request, 'pages/mobile.html') 

@staff_member_required
def tablet(request):
    return render(request, 'pages/tablet.html') 

@staff_member_required
def laptop(request):
    return render(request, 'pages/laptop.html') 