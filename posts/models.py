from django.db import models
from django.utils import timezone

from accounts.models import Accounts
# Create your models here.

class Post(models.Model):

  title = models.CharField(verbose_name='title', max_length=100, blank=False)
  detail = models.CharField(verbose_name='detail', max_length=255, blank=True)
  limit = models.DateField(verbose_name='limit', auto_now=False, auto_now_add=False, blank=True)
  user = models.ForeignKey(Accounts, verbose_name='user', on_delete=models.CASCADE, related_name='posts')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # class Meta(object):
  #   db_table = 'post'

  def __str__(self):
    return self.title

class Task(models.Model):

  content = models.CharField(verbose_name='content', max_length=255, blank=True)
  is_done = models.BooleanField(verbose_name='content', default=False)
  post = models.ForeignKey(Post, verbose_name='post_id', on_delete=models.CASCADE, related_name="tasks")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # class Meta(object):
  #   db_table = 'posts'

  def __str__(self):
    return self.content

