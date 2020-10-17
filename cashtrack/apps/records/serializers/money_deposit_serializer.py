from rest_framework import serializers

from ..models import MoneyDeposit

class MoneyDepositSerializer(serializers.HyperlinkedModelSerializer):
    records = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='record-detail')
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = MoneyDeposit
        fields = ['url', 'owner', 'name', 'initial_amount', 'records']