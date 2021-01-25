from rest_framework import routers
from django.urls import path, include

from .views import FavoriteAPI

urlpatterns = [
  path('<int:user_id>/', FavoriteAPI.as_view()),
]