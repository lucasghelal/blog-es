from django.conf.urls import url
from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
    url(r'^blog/$', views.post_list, name='post_list'),
    # url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    url(r'^blog/(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    url(r'^blog/tag/(?P<tag_slug>[-\w]+)/$',
        views.post_list,
        name='post_list_by_tag'),
    url(r'^blog/feed/$', LatestPostsFeed(), name='post_feed'),
    url(r'^blog/search/$', views.post_search, name='post_search'),
    url(r'^blog/new/$', views.post_new, name='post_new'),
    ]
