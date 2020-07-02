from rest_framework import serializers
from account.models import Info as User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = '__all__'


class OtcAccountListSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = User
        # fields = ['id', 'nickname', 'margin_amount','date_joined', 'last_login',
        #           'trade_count', 'month_trade_count', 'buy_trade_count','sell_trade_count',
        #           'order_complete_rate', 'release_time_avg', 'cancel_time_avg',]
        fields = '__all__'

class OtcAccountDetailSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = User
        # fields = ['id', 'nickname', 'margin_amount', 'date_joined', 'last_login',
        #           'trade_count', 'month_trade_count', 'buy_trade_count', 'sell_trade_count',
        #           'order_complete_rate', 'release_time_avg', 'cancel_time_avg', ]
        fields = '__all__'



                #created = models.DateTimeField(auto_now_add=True)
    #title = models.CharField(max_length=100, blank=True, default='')
    #code = models.TextField()
    #linenos = models.BooleanField(default=False)
    #language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    #style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)


# from django.contrib.auth.models import User
#
# class OtcAccountSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=OtcAccount.objects.all())
#
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets']