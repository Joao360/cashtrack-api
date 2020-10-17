from django.db.models import Sum, When, Case
from rest_framework import serializers

from ..models import MoneyDeposit, Record

class MoneyDepositSerializer(serializers.HyperlinkedModelSerializer):
    records = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='record-detail')
    owner = serializers.ReadOnlyField(source='owner.email')
    amount = serializers.SerializerMethodField()

    class Meta:
        model = MoneyDeposit
        fields = ['url', 'owner', 'name', 'initial_amount', 'amount', 'records']

    def get_amount(self, obj):
        values = Record.objects.filter(money_deposit=obj).aggregate(
            income=Sum(
                Case(When(recordType='Income', then='amount'))
                ), 
            expense=Sum(
                Case(When(recordType='Expense', then='amount'))
            ),
        )

        return obj.initial_amount + values['income'] - values['expense']
