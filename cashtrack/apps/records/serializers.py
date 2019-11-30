from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Category, Subcategory, Record, RECORD_TYPES

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class RecordSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Record
        field = ['id', 'recordType', 'ammount', 'datetime', 'note', 'entity', 'category']