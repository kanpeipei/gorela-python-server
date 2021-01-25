from rest_framework import serializers

from accounts.serializers import AccountsSerializer
from .models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
  user = AccountsSerializer(read_only=True)

  class Meta:
    model = Favorite
    fields = ['user']

