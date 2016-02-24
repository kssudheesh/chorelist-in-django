from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^newlist/$', views.newlist, name='newlist'),
    url(r'^(?P<chorelist_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<chorelist_id>[0-9]+)/deletelist/$', views.deletelist, name='deletelist'),
    url(r'^(?P<chorelist_id>[0-9]+)/newchore/$', views.newchore, name='newchore'),
    url(r'^(?P<chorelist_id>[0-9]+)/chores/(?P<chore_id>[0-9]+)/$', views.choredetail, name='choredetail'),
    url(r'^(?P<chorelist_id>[0-9]+)/chores/(?P<chore_id>[0-9]+)/update/$', views.updatechore, name='updatechore'),
    url(r'^(?P<chorelist_id>[0-9]+)/chores/(?P<chore_id>[0-9]+)/deletechore/$', views.deletechore, name='deletechore'),

]
