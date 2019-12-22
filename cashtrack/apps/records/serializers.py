from rest_framework.serializers import ModelSerializer, ReadOnlyField

from .models import Record


class RecordSerializer(ModelSerializer):
    owner = ReadOnlyField(source='owner.username')

    class Meta:
        model = Record
        fields = ['owner', 'id', 'recordType', 'ammount', 'datetime', 'note', 'entity', 'category']
