from rest_framework import routers
from django.urls import path, include

from .views import GetPostAPI, PostsAPI, AddPostAPI

urlpatterns = [
    path('', PostsAPI.as_view()),
    path('create/', AddPostAPI.as_view()),
    path('<int:pk>/', GetPostAPI.as_view()),
    path('<int:pk>/comment/', include('comments.urls')),
]
