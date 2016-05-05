from django.conf.urls import url

from promises import views

urlpatterns = [
    url(r'^$', views.ViewPromise.as_view(), name='view'),
    url(r'^edit/$', views.EditPromise.as_view(), name='edit'),
]
