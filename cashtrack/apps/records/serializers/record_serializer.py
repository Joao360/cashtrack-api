from rest_framework.serializers import ReadOnlyField, HyperlinkedModelSerializer

from ..models import Record


class RecordSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = [
            "url",
            "money_deposit",
            "id",
            "recordType",
            "amount",
            "datetime",
            "note",
            "entity",
            "category",
        ]
