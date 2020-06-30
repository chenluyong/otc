from rest_framework import serializers
from history.models import Info as History, DepositWithdraw



class HistoryDetailSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = History
        # fields = ['id', 'user', 'coin_name','type', 'transact_type',
        #           'amount', 'fee', 'available_balance','account_balance',
        #           'prev_history_id', 'transact_at']
        fields = '__all__'


class DepositWithdrawHistoryListSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = DepositWithdraw
        # fields = ['id', 'type', 'txid','blockchain', 'coin_name',
        #           'amount', 'fee', 'address','address_tag',
        #           'status', 'error_code', 'error_message',
        #           'created_at','updated_at']
        fields = '__all__'


