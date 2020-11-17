from rest_framework import serializers

from .models import Accounts, AccountsManager


class AccountsSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Accounts
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        return Accounts.objects.create_user(validated_data['username'],validated_data['password'])