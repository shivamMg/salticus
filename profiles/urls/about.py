from django.conf.urls import url

from promises.views import create_promise
from  .. import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.ViewProfile.as_view(), name='about'),
    url(r'^about/edit/$', views.EditProfile.as_view(), name='edit'),

    url(r'^submit/$', create_promise, name='create_promise'),
]
