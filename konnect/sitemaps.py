from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ['index', 'about_view', 'services_view', 'contact', 'privacy_policy']

    def location(self, item):
        return reverse(item)