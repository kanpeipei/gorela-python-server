from django.db import transaction
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Favorite
from posts.models import Post
from accounts.models import Accounts

# Create your views here.
class FavoriteAPI(APIView):
  @transaction.atomic
  def get_object(self, model, pk):
    try:
      return model.objects.get(pk=pk)
    except model.DoesNotExist:
      raise Http404

  def post(self, request, post_id, user_id, format=None):
    post = self.get_object(Post, post_id)
    user = self.get_object(Accounts, user_id)
    favorite = Favorite.objects.create(post=post, user=user)
    return Response(status=status.HTTP_201_CREATED)

  def delete(self, request, post_id, user_id, format=None):
    post = self.get_object(Post, post_id)
    user = self.get_object(Accounts, user_id)
    favorite = Favorite.objects.filter(post=post, user=user)
    favorite.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


