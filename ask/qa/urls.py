from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.test, name='root'),
    url(r'^login/$', views.test, name='root'),
    url(r'^signup/$', views.test, name='root'),
    url(r'^question/\d+/$', views.test, name='root'),
    url(r'^ask/$', views.test, name='root'),
    url(r'^popular/$', views.test, name='root'),
    url(r'^new/$', views.test, name='root'),
]
