from django.conf.urls import url, include

from profiles import views

urlpatterns = [
    # Profile
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.ViewProfile.as_view(), name='about'),
    url(r'^about/edit/$', views.EditProfile.as_view(), name='edit'),

    # Promises
    url(r'^promises/', include('promises.urls.promises',
                               namespace='promises')),

    # A Promise
    url(r'^promise/(?P<base36_id>[a-z\d]+)/', include('promises.urls.promise',
                                                      namespace='promise')),
]
