from rest_framework import routers
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from .views import AddAccountAPI

urlpatterns = [
    url(r'signup', AddAccountAPI.as_view()),
]
