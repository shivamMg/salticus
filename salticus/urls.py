from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.views.generic import TemplateView

from users import views as user_views
from .settings.dev import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    # User Auth
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
    url(r'^account/$', user_views.account_info, name='account'),

    # Profiles
    url(r'^profiles/', include('profiles.urls.profiles',
                               namespace='profiles')),

    # A Profile
    url(r'^p/(?P<handle>[-\w]+)/', include('profiles.urls.profile',
                                           namespace='profile')),

    # Homepage
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
