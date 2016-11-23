from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url(r'^(?P<page>\d+)/$', views.news, name='news'),
    url(r'^login/$', views.test, name='root'),
    url(r'^signup/$', views.test, name='root'),
    url(r'^question/(?P<pk>\d+)/$', views.question_detail, name='question_detail'),
    url(r'^ask/$', views.test, name='root'),
    url(r'^popular/$', views.popular, name='popular'),
    url(r'^new/$', views.test, name='root'),

]
