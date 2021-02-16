from django.db import transaction
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Post, Task
from .serializers import PostSerializer, TaskSerializer
from accounts.models import Accounts


# Create your views here.
class GetPostsAPI(APIView):
  serializer_class = PostSerializer

  def get(self, request, format=None):
    posts = Post.objects.order_by('-created_at').prefetch_related("tasks")
    serializer = self.serializer_class(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class PostAPI(APIView):
  serializer_class = PostSerializer

  @transaction.atomic
  def get_object(self, pk):
    try:
      return Post.objects.get(pk=pk)
    except Post.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    post = self.get_object(pk)
    serializer = self.serializer_class(post)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def delete(self, request, pk, format=None):
    post = self.get_object(pk)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class AddPostAPI(APIView):
  serializer_class = PostSerializer

  def post(self, request, format=None):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SwitchTaskAPI(APIView):
  serializer_class = TaskSerializer

  @transaction.atomic
  def get_object(self, pk):
    try:
      return Task.objects.get(pk=pk)
    except Task.DoesNotExist:
      raise Http404


  def put(self, request, pk, format=None):
    task = self.get_object(pk)
    serializer = self.serializer_class(task, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
