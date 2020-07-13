# from rest_framework import serializers
# from balance.models import History as BalanceHistoryModel
#
#
# class BalanceHistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BalanceHistoryModel
#
#         fields = '__all__'
#
#
# class BalanceDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BalanceHistoryModel
#
#         fields = '__all__'



########################################

class BalanceUpdateRequestSerializer():

    def __init__(self, *args, **kwargs):
        self.user_id = None
        self.coin_name = None
        self.business = None
        self.business_id = None
        self.change = None
        self.detail = None
        try:
            self.user_id = args[0]
            self.coin_name = args[1]
            self.business = args[2]
            self.business_id = args[3]
            self.change = args[4]
            self.detail = args[5]
        except IndexError as e:
            pass


    def __str__(self):
        pass