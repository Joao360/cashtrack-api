from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework import permissions, viewsets

from .models import Record, Category, MoneyDeposit
from .serializers import RecordSerializer, CategorySerializer, MoneyDepositSerializer
from .permissions import IsRecordOwner

class RecordList(ListCreateAPIView):
    """
    This view should return a list of all the records
    for the currently authenticated user.
    """
    serializer_class = RecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Record.objects.filter(money_deposit__owner=self.request.user)

class RecordDetail(RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [permissions.IsAuthenticated, IsRecordOwner]

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class CategoryDetail(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class MoneyDepositViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing money deposit instances.
    """
    serializer_class = MoneyDepositSerializer
    queryset = MoneyDeposit.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MoneyDeposit.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)