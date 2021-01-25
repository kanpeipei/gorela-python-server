from django.db import models
from django.utils import timezone

from accounts.models import Accounts
from posts.models import Post
# Create your models here.

class Favorite(models.Model):

  post = models.ForeignKey(Post, verbose_name='post', on_delete=models.CASCADE, related_name='favorites')
  user = models.ForeignKey(Accounts, verbose_name='user', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # class Meta(object):
  #   db_table = 'post'

  def __str__(self):
    return self.post.title
