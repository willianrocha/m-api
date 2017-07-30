from django.conf.urls import include, url

from . import views

app_name = 'comics'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^character/(?P<char_id>[0-9]+)/$', views.character, name='character'),
    url(r'^story/(?P<story_id>[0-9]+)/$', views.story, name='story'),
    url(r'^comic/(?P<comic_id>[0-9]+)/$', views.comic, name='comic'),
]
