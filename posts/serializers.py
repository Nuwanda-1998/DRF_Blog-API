from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Post




class PostSerializer(serializers.ModelSerializer):
    'Serializing the post object'
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at',)



class UserSerializer(serializers.ModelSerializer):
    'Serializing the Users Object'
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)