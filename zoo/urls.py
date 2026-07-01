from django.urls import path
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from . import views

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return ['index', 'privacy_policy']

    def location(self, item):
        return reverse(item)

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.index_view, name='index'),
    path('relocation/submit/', views.process_relocation_view, name='process_relocation'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/submit/', views.process_contact_view, name='process_contact'),
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]