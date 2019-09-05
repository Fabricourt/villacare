from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as profile_views
from contact.views import Contact
from django.contrib.sitemaps.views import sitemap
from listings.sitemaps import StaticViewSitemap
from companies.sitemaps import StaticViewSitemap
from realtors.sitemaps import StaticViewSitemap
from rentals.sitemaps import StaticViewSitemap
from houses.sitemaps import StaticViewSitemap
from testimonials.views import testimonial



sitemaps = {
    'static': StaticViewSitemap
}



urlpatterns = [
    path('', include('pages.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path('blog/',  include('blog.urls')),
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('contact/', Contact, name="contact"),
    path('contact/', include('contact.urls')),
    path('companies/', include('companies.urls')),
    path('gallerys/', include('gallerys.urls')),
    path('houses/', include('houses.urls')),
    path('rentals/', include('rentals.urls')),
    path('admin/', admin.site.urls),
    path('profile/', profile_views.profile, name='profile' ),
    path('testimonial/', testimonial, name='testimonial'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    