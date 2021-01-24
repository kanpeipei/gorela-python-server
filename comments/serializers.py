from rest_framework import serializers

from .models import Comment
from accounts.models import Accounts
from accounts.serializers import AccountsSerializer
from posts.models import Post

class CommentSerializer(serializers.ModelSerializer):
  user = AccountsSerializer(read_only=True)
  user_id = serializers.PrimaryKeyRelatedField(queryset=Accounts.objects.all(), write_only=True)
  post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)

  class Meta:
    model = Comment
    fields = ['content', 'user', 'user_id', 'post_id']

  def create(self, validated_data):
    validated_data['user'] = validated_data.get('user_id', None)
    if validated_data['user'] is None:
      raise serializers.ValidationError("user not found.")
    del validated_data['user_id']
    validated_data['post'] = validated_data.get('post_id', None)
    if validated_data['post'] is None:
      raise serializers.ValidationError("post not found.")
    del validated_data['post_id']
    comment = Comment.objects.create(**validated_data)
    return comment