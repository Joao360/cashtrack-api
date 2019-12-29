from rest_framework.serializers import ReadOnlyField, HyperlinkedModelSerializer

from ..models import Record


class RecordSerializer(HyperlinkedModelSerializer):
    owner = ReadOnlyField(source='owner.username')

    class Meta:
        model = Record
        fields = ['url', 'owner', 'id', 'recordType', 'ammount', 'datetime', 'note', 'entity', 'category']
