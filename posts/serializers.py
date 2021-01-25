from rest_framework import serializers

from .models import Post, Task
from accounts.models import Accounts
from accounts.serializers import AccountsSerializer
from comments.serializers import CommentSerializer
from favorites.serializers import FavoriteSerializer
class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = ['id', 'content', 'is_done']

class PostSerializer(serializers.ModelSerializer):
  user = AccountsSerializer(read_only=True)
  user_id = serializers.PrimaryKeyRelatedField(queryset=Accounts.objects.all(), write_only=True)
  tasks = TaskSerializer(many=True)
  comments = CommentSerializer(many=True, read_only=True)
  favorites = FavoriteSerializer(many=True, read_only=True)

  class Meta:
    model = Post
    fields = ['id', 'title', 'detail', 'limit', 'user', 'user_id', 'tasks', 'comments', 'favorites']

  def create(self, validated_data):
    tasks_data = validated_data.pop('tasks')
    validated_data['user'] = validated_data.get('user_id', None)
    if validated_data['user'] is None:
      raise serializers.ValidationError("user not found.")
    del validated_data['user_id']

    post = Post.objects.create(**validated_data)
    for task_data in tasks_data:
      Task.objects.create(post=post, **task_data)
    return post

class PostByAccountSerializer(serializers.ModelSerializer):
  tasks = TaskSerializer(many=True)
  comments = CommentSerializer(many=True, read_only=True)
  favorites = FavoriteSerializer(many=True, read_only=True)

  class Meta:
    model = Post
    fields = ['id', 'title', 'detail', 'limit', 'tasks', 'comments', 'favorites']

class AccountDetailSerializer(serializers.ModelSerializer):
    posts = PostByAccountSerializer(many=True, read_only=True)

    class Meta:
        model = Accounts
        fields = ('username', 'introduction', 'image', 'posts')