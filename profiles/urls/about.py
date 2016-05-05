from django.conf.urls import url

from promises.views import create_promise, ViewPromise, EditPromise
from  .. import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.ViewProfile.as_view(), name='about'),
    url(r'^about/edit/$', views.EditProfile.as_view(), name='edit'),

    url(r'^submit/$', create_promise, name='create_promise'),
    url(r'^promises/(?P<base36_id>[a-z\d]+)/edit/$', EditPromise.as_view(),
        name='edit_promise'),
    url(r'^promises/(?P<base36_id>[a-z\d]+)/$', ViewPromise.as_view(),
        name='view_promise'),
]
