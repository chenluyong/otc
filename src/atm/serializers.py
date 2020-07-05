from rest_framework import serializers
from atm.models import History as AtmHistoryModel


class AtmHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AtmHistoryModel

        fields = '__all__'


class AtmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtmHistoryModel

        fields = '__all__'
