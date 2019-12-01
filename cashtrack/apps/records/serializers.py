from django.contrib.auth.models import User, Group
from rest_framework.serializers import ModelSerializer

from .models import Category, Subcategory, Record, RECORD_TYPES


class RecordSerializer(ModelSerializer): 
    class Meta:
        model = Record
        field = ['owner', 'id', 'recordType', 'ammount', 'datetime', 'note', 'entity', 'category']