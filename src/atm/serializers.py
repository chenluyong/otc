from rest_framework import serializers
from atm.models import History as AtmHistoryModel


class AtmHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AtmHistoryModel

        fields = ['id', 'blockchain', 'coin_name','txid', 'address',
                  'type', 'actual_amount', 'status','created_at',
                  'updated_at','user_id']

