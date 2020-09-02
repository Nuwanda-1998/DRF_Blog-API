from rest_framework import generics

from .serializers import PostSerializer, UserSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly

from django.contrib.auth import get_user_model



class PostList(generics.ListCreateAPIView):
    'List avalible Posts and make add new post function'
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    'show the detail of the posts and make update and delete function'
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
    'Displaying the List of Users'
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    'Display the Detail of Specific User'
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
