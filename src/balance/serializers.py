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
from django.utils.translation import gettext_lazy as _

from balance import app_settings
from utils.error import BalanceException
import sys



class BalanceBase():
    pass

class BalanceHistorySerializer():
    _user_id = None
    _coin_name = None
    _business = None
    _business_id = None
    _change = None
    _balance = None
    _freeze_balance = None
    _change_at = None
    _detail = None

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if value is None or value == 0:
            raise BalanceException(_("user_id can't to be {0}").format(value)).PARAMETER_ERROR
        self._user_id = value

    @property
    def coin_name(self):
        return self._coin_name

    @coin_name.setter
    def coin_name(self, value):
        if value and value not in app_settings.SUPPORT_ASSETS:
            raise BalanceException(_("Not support the {0} coin").format(value)).ASSET_NOT_SUPPORT
        self._coin_name = value

    @property
    def business(self):
        return self._business

    @business.setter
    def business(self, value):
        self._business = value

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value

    @property
    def change(self):
        return self._change

    @change.setter
    def change(self, value):
        v = float(value)
        if v == 0:
            raise BalanceException(_("{0} can't change").format(value)).CHANGE_ERROR
        self._change = v
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    @property
    def freeze_balance(self):
        return self._freeze_balance

    @freeze_balance.setter
    def freeze_balance(self, value):
        self._freeze_balance = value


    @property
    def change_at(self):
        return self._change_at

    @change_at.setter
    def change_at(self, value):
        self._change_at = value

    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = value

class BalanceUpdateRequestSerializer(BalanceHistorySerializer):
    def __init__(self,  *args, **kwargs):
        try:
            self.user_id = args[0]
            self.coin_name = args[1]
            self.business = args[2]
            self.business_id = args[3]
            self.change = args[4]
            self.detail = args[5]
        except IndexError as e:
            pass


class BalanceHistoryRequestSerializer(BalanceHistorySerializer):
    _start_time = 0
    _end_time = sys.maxsize
    _offset = 0
    _limit = 25

    @property
    def start_time(self):
        return self._start_time
    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    @property
    def end_time(self):
        return self._end_time
    @end_time.setter
    def end_time(self, value):
        self._end_time = value

    @property
    def offset(self):
        return self._offset
    @offset.setter
    def offset(self, value):
        self._offset = value

    @property
    def limit(self):
        return self._limit
    @limit.setter
    def limit(self, value):
        self._limit = value

    def __init__(self, *args, **kwargs):
        try:
            self.user_id = args[0]
            self.coin_name = args[1]
            self.business = args[2]
            self.start_time = args[3]
            self.end_time = args[4]

            if args[5]:
                self.offset = args[5]
            if args[6]:
                self.limit = args[6]

        except IndexError as e:
            pass