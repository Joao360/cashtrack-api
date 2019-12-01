from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Record
from .serializers import RecordSerializer


class RecordList(ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class RecordDetail(RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
