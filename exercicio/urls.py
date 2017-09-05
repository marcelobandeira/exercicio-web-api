from django.conf.urls import url, include
from exercicio import views
from rest_framework import routers

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/$', 
        views.UserList.as_view(), 
        name=views.UserList.name),
    url(r'^users/(?P<pk>[0-9]+)/$', 
        views.UserDetail.as_view(),
        name=views.UserDetail.name),
    url(r'^posts/$', 
        views.PostList.as_view(), 
        name=views.PostList.name),
    url(r'^posts/(?P<pk>[0-9]+)/$', 
        views.PostDetail.as_view(),
        name=views.PostDetail.name), 
    url(r'^comments/$', 
        views.CommentList.as_view(), 
        name=views.CommentList.name),
    url(r'^comments/(?P<pk>[0-9]+)/$', 
        views.CommentDetail.as_view(),
        name=views.CommentDetail.name), 
    url(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
]
