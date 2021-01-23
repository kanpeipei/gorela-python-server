from rest_framework import routers
from django.conf.urls import url
from django.urls import path

from .views import GetPostAPI, PostsAPI, AddPostAPI

urlpatterns = [
    url(r'create/', AddPostAPI.as_view()),
    url(r'', PostsAPI.as_view()),
    path('<int:pk>/', GetPostAPI.as_view()),
]
