from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Core
    url(r'^', include('core.urls')),

    # Contact
    url('^contact/$',
        TemplateView.as_view(template_name='contact/contact.html'),
        name='contact'),

    # Registration
    url(r'^', include('registration.urls')),

    # Sitemap
    url(r'^', include('sitemap.urls')),

    # Tinymce
    url(r'^tinymce/', include('tinymce.urls')),

    # Captcha
    url(r'^captcha/', include('captcha.urls')),
]
