from django.shortcuts import render,  redirect
from django.contrib import messages
from .models import Testimonial
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required

@login_required
def testimonial(request):
    template ="testimonials.html"
    testimonials = Testimonial.objects.order_by('-post_date').filter(is_published=True)
    context ={
        'testimonials':testimonials,
    }

    return render (request,  template, context)

