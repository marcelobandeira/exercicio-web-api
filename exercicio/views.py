from django.utils import timezone
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import render
from rest_framework.views import APIView

from exercicio.serializers import *
from exercicio.models import *

from django.contrib.auth.models import User
from rest_framework import permissions
from exercicio.permissions import IsOwnerOrReadOnly, IsPostOwnerOrReadOnly

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-list'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-detail'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	name = 'post-list'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	name = 'post-detail'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class CommentList(generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	name = 'comment-list'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsPostOwnerOrReadOnly)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request,*args, **kwargs):
        return Response({
            'users': reverse(UserList.name, request=request),
            'posts': reverse(PostList.name, request=request),
            'comments': reverse(CommentList.name, request=request),
            })


# def add_auth_user():
#     users = UserOld.objects.all()

#     for userold in users:

#         print userold.username
#         user = User(
#             email=userold.email, is_staff=False, is_active=True,
#             is_superuser=False, username=userold.username)

#         user.set_password('password123')
#         user.save()

#         print user.email


# def import_data():
#     dump_data = open('db.json', 'r')
#     as_json = json.load(dump_data)

    # for user in as_json['users']:
    #     geo = Geo.objects.create(lat=user['address']['geo']['lat'],
    #                              lng=user['address']['geo']['lng'])
    #     address = Address.objects.create(street=user['address']['street'],
    #                                      suite=user['address']['suite'],
    #                                      city=user['address']['city'],
    #                                      zipcode=user['address']['zipcode'],
    #                                      geo=geo)
    #     User.objects.create(id=user['id'],
    #                         name=user['name'],
    #                         username=user['username'],
    #                         email=user['email'],
    #                         address=address)

    # for post in as_json['posts']:
    #     user = User.objects.get(id=post['userId'])
    #     Post.objects.create(id=post['id'],
    #                         title=post['title'],
    #                         body=post['body'],
    #                         user=user)

    # for comment in as_json['comments']:
    #     post = Post.objects.get(id=comment['postId'])
    #     Comment.objects.create(id=comment['id'],
    #                            name=comment['name'],
    #                            email=comment['email'],
    #                            body=comment['body'],post=post)
