from django.urls import path, re_path
from trackerMain.views import *
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'), #REMOVE
    path('api/item', item.as_view()),
    path('api/address', address.as_view()),
    path('api/transfer', transfer.as_view()),
    path('startNode', views.startNode, name='startNode'),
    path('middleNode', views.middleNode, name='middleNode'),
    path('endNode', views.endNode, name='endNode'),
    re_path(r'^test/(?P<iID>\w{1,50})/$', views.endNode, name='endNode'),
    path('test', views.test, name='test'), #REMOVE
    re_path(r'^test/(?P<iID>\w{1,50})/(?P<nID>\w{1,50})/$', views.test, name='test2'), #REMOVE
]