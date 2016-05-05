from django.conf.urls import url

from promises.views import create_promise

urlpatterns = [
    url(r'^submit/$', create_promise, name='create'),
]
