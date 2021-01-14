from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Accounts
from .serializers import AccountsSerializer


# Create your views here.
class AddAccountAPI(APIView):
  permission_classes = (permissions.AllowAny,)
  serializer_class = AccountsSerializer

  @transaction.atomic
  def post(self, request):
    serializer = AccountsSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAccountAPI(APIView):
  permissions_classes = (permissions.AllowAny,)
  serializer_class = AccountsSerializer

  @transaction.atomic
  def get_object(self, pk):
    try:
      return User.objects.get(pk=pk)
    except User.DoesNotExist:
      raise Http404

  @transaction.atomic
  def get(self, request, pk, format=None):
    user = self.get_object(pk)
    serializer = self.serializer_class(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


