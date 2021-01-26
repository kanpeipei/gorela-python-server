from rest_framework import serializers

from .models import Accounts, AccountsManager, Relation


class AccountsSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Accounts
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        return Accounts.objects.create_user(validated_data['username'],validated_data['password'])

class FollowAccountSerializer(serializers.ModelSerializer):
    # follow_user = AccountsSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=Accounts.objects.all(), write_only=True)
    target_user_id = serializers.PrimaryKeyRelatedField(queryset=Accounts.objects.all(), write_only=True)

    class Meta:
        model = Relation
        fields = ('id', 'user', 'user_id', 'target_user_id')

    def create(self, validated_data):
        validated_data['user'] = validated_data.get('user_id', None)
        if validated_data['user'] is None:
            raise serializers.ValidationError("user not found.")
        del validated_data['user_id']

        validated_data['target_user'] = validated_data.get('target_user_id', None)
        if validated_data['target_user'] is None:
            raise serializers.ValidationError("target user not found.")
        del validated_data['target_user_id']

        relation = Relation.objects.create(**validated_data)
        return relation

class FollowerAccountSerializer(serializers.ModelSerializer):
    # followed_user = AccountsSerializer(read_only=True)

    class Meta:
        model = Relation
        fields = ('id', 'target_user')

