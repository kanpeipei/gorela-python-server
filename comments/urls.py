from rest_framework import routers
from django.urls import path

from .views import AddCommentAPI

urlpatterns = [
    path('', AddCommentAPI.as_view()),
]
