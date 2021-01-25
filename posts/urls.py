from rest_framework import routers
from django.urls import path, include

from .views import PostAPI, GetPostsAPI, AddPostAPI, SwitchTaskAPI

urlpatterns = [
    path('', GetPostsAPI.as_view()),
    path('create/', AddPostAPI.as_view()),
    path('<int:pk>/', PostAPI.as_view()),
    path('tasks/<int:pk>/', SwitchTaskAPI.as_view()),
    path('<int:pk>/comment/', include('comments.urls')),
    path('<int:post_id>/favorite/', include('favorites.urls')),
]
