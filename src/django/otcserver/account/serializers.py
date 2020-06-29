from rest_framework import serializers
from account.models import UserInfo

class AccountSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = UserInfo
        # fields = ['id', 'phone', 'recently_trade_count', 'last_trade_time','owner']


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