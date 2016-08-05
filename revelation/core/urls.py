from django.contrib.auth.decorators import login_required
from django.conf.urls import url
import views

urlpatterns = [

    url(r'public/$',
        views.RevelationModelListView.as_view(),
        name='revelation-list'),

    url(r'u/(?P<pk>\d+)/$',
        views.UserProfileView.as_view(),
        name='user-view'),

    url(r'delete/(?P<pk>\d+)/$',
        login_required(views.RevelationModelDeleteView.as_view()),
        name='revelation-delete'),

    url(r'create/$', views.RevelationModelCreateView.as_view(),
        name='revelation-create'),

    url(r'r/(?P<pk>\d+)/$',
        views.RevelationModelDetailView.as_view(),
        name='revelation-view'),

    url(r'^$',
        views.HomePageView.as_view(),
        name='home'),

]
