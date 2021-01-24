from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Comment
from .serializers import CommentSerializer
from posts.models import Post

# Create your views here.
class AddCommentAPI(APIView):
  serializer_class = CommentSerializer

  def post(self, request, pk, format=None):
    request.data['post_id'] = pk
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
