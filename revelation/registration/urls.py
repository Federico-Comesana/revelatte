from django.contrib.auth import views as auth_views
from views import registration_form
from django.conf.urls import url

urlpatterns = [

    # Registration
    url(r'signup/$', registration_form, name="signup"),

    url(r'login/$', auth_views.login, name="login"),

    url(r'logout/$', auth_views.logout, {'next_page': '/'}, name="logout", )

]
