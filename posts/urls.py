from rest_framework import routers
from django.conf.urls import url
from django.urls import path

from .views import GetPostAPI, GetPostsAPI

urlpatterns = [
    url(r'', GetPostsAPI.as_view()),
    path('<int:pk>/', GetPostAPI.as_view()),
]
