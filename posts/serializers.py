from rest_framework import serializers

from .models import Posts, Tasks

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tasks
    fields = ['content']

class PostSerializer(serializers.ModelSerializer):
  tasks = TaskSerializer(many=True)

  class Meta:
    model = Posts
    fields = ['title', 'detail', 'limit', 'tasks']

  def create(self, validated_data):
    tasks_data = validated_data.pop('tasks')
    post = Posts.objects.create(**validated_data)
    for task_data in tasks_data:
      Tasks.objects.create(post=post, **task_data)
    return album