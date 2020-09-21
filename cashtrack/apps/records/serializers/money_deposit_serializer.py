from rest_framework import serializers

from ..models import MoneyDeposit

class MoneyDepositSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MoneyDeposit
        fields = ['url', 'owner', 'name', 'ammount']