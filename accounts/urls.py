from rest_framework import routers
from django.conf.urls import url
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from .views import AddAccountAPI, GetAccountAPI, UpdateAccountAPI, RelationAPI

urlpatterns = [
    url(r'signup/', AddAccountAPI.as_view()),
    path('<int:pk>/', GetAccountAPI.as_view()),
    path('<int:pk>/edit/', UpdateAccountAPI.as_view()),
    path('follow/<int:user_id>/<int:target_user_id>/', RelationAPI.as_view()),
]
