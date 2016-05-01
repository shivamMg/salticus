from django.conf.urls import url

from profiles.views import create_profile

urlpatterns = [
    url(r'^create/$', create_profile, name='create'),
]
