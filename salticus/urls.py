from django.conf.urls import url
from django.contrib.auth import views as auth_views

from users import views as user_views

urlpatterns = [
    url(
        r'^login/$',
        auth_views.login,
        name='login',
        kwargs={'template_name': 'users/login.html'},
    ),
    url(
        r'^logout/$',
        auth_views.logout,
        name='logout',
        kwargs={'next_page': '/'},
    ),
    url(
        r'^signup/$',
        user_views.signup,
        name='signup',
    ),
    url(r'^account/$', user_views.account, name='account'),
]
