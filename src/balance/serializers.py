from rest_framework import serializers
from balance.models import History as BalanceHistoryModel


class BalanceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceHistoryModel

        fields = '__all__'


class BalanceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceHistoryModel

        fields = '__all__'
