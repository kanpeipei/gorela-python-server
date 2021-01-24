from django.db import models
from django.utils import timezone

from accounts.models import Accounts
from posts.models import Post
# Create your models here.

class Comment(models.Model):

  content = models.CharField(verbose_name='content', max_length=255, blank=False)
  user = models.ForeignKey(Accounts, verbose_name='user', on_delete=models.CASCADE)
  post = models.ForeignKey(Post, verbose_name='post', on_delete=models.CASCADE, related_name='comments')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.content
