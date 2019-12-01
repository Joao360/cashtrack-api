from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import UserSerializer


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer