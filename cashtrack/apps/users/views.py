from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from .serializers import UserSerializer


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
