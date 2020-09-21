from rest_framework.serializers import ReadOnlyField, HyperlinkedModelSerializer

from ..models import Record


class RecordSerializer(HyperlinkedModelSerializer):
    money_deposit = ReadOnlyField(source='money_deposit.name')

    class Meta:
        model = Record
        fields = ['url', 'money_deposit', 'id', 'recordType', 'ammount', 'datetime', 'note', 'entity', 'category']
