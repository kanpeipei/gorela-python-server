from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Accounts, Relation
from .serializers import AccountsSerializer, UpdateAccountSerializer, FollowAccountSerializer
from posts.serializers import AccountDetailSerializer


# Create your views here.
class AddAccountAPI(APIView):
  permission_classes = (permissions.AllowAny,)
  serializer_class = AccountsSerializer

  def post(self, request):
    serializer = AccountsSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAccountAPI(APIView):
  serializer_class = AccountDetailSerializer

  @transaction.atomic
  def get_object(self, pk):
    try:
      return Accounts.objects.get(pk=pk)
    except Accounts.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    user = self.get_object(pk)
    serializer = self.serializer_class(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateAccountAPI(APIView):
  serializer_class = UpdateAccountSerializer

  @transaction.atomic
  def get_object(self, pk):
    try:
      return Accounts.objects.get(pk=pk)
    except Accounts.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    user = self.get_object(pk)
    serializer = self.serializer_class(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def put(self, request, pk, format=None):
    user = self.get_object(pk)
    serializer = self.serializer_class(user, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RelationAPI(APIView):
  @transaction.atomic
  def get_object(self, pk):
    try:
      return Accounts.objects.get(pk=pk)
    except Accounts.DoesNotExist:
      raise Http404

  def post(self, request, user_id, target_user_id):
    request.data['user_id'] = user_id
    request.data['target_user_id'] = target_user_id
    serializer = FollowAccountSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, user_id, target_user_id):
    user = self.get_object(user_id)
    target_user = self.get_object(target_user_id)
    relation = Relation.objects.filter(user=user, target_user=target_user)
    relation.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

