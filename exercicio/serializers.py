from rest_framework import serializers
from exercicio.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = (
        	'url',
            'username',
            'name',
            'email',
            'posts'
        )

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'url',
            'body',
            'email',
            'name',
        )

class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    class Meta:
        model = Post
        fields = (
            'url',
            'body',
            'title',
            'user',
            'comments'
        )