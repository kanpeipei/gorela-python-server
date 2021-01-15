from django.db import transaction
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Posts, Tasks
from .serializers import PostSerializer, TaskSerializer


# Create your views here.
class GetPostsAPI(APIView):
  permissions_classes = (permissions.AllowAny,)
  serializer_class = PostSerializer

  @transaction.atomic
  def get(self, request, format=None):
    posts = Posts.objects.all()
    serializer = self.serializer_class(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class GetPostAPI(APIView):
  permissions_classes = (permissions.AllowAny,)
  serializer_class = PostSerializer

  @transaction.atomic
  def get_object(self, pk):
    try:
      return Posts.objects.get(pk=pk)
    except Posts.DoesNotExist:
      raise Http404

  @transaction.atomic
  def get(self, request, pk, format=None):
    post = self.get_object(pk)
    serializer = self.serializer_class(post)
    return Response(serializer.data, status=status.HTTP_200_OK)
