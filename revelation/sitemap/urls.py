from django.conf.urls import url
from django.contrib.sitemaps import GenericSitemap
from core.models import RevelationModel

revelation_sitemap = {
    'queryset': RevelationModel.objects.filter(public=True),
    'date_field': 'created',
}

sitemaps = {
    'revelations': GenericSitemap(revelation_sitemap, priority=0.5),
}

urlpatterns = [
    # the sitemap
    url(r'sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
