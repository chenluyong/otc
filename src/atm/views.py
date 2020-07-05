from django.shortcuts import render
from django.shortcuts import redirect,reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

# Create your views here.
from atm.models import History as AtmHistoryModel
from atm.serializers import AtmHistorySerializer

from utils import JsonResponse
from utils.http_code import *
from atm.services import get_address

class AtmHistoryListView(
                    mixins.ListModelMixin,
                    generics.GenericAPIView):

    queryset = AtmHistoryModel.objects.all()
    serializer_class = AtmHistorySerializer

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        if user_id is None:
            return JsonResponse(None, HTTP_CODE_UNAUTHORIZED)

        self.queryset = AtmHistoryModel.objects.all().filter(user_id=user_id)
        print(self.queryset)
        return JsonResponse(self.list(request, *args, **kwargs).data)


class AtmHistoryDetailView(APIView):


    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        atm_id = int(kwargs['atm_id'])
        if user_id is None:
            return JsonResponse(None, HTTP_CODE_UNAUTHORIZED)

        try:
            atm_history = AtmHistoryModel.objects.get(user_id=user_id, id=atm_id)
        except Exception as e:
            return JsonResponse(None,HTTP_CODE_NOT_FOUND,e.args[0])


        # return JsonResponse(atm_history)
        return JsonResponse({
            'id':atm_history.id,
            'blockchain':atm_history.blockchain,
            'coin_name':atm_history.coin_name,
            'txid':atm_history.txid,
            'address':atm_history.address,
            'address_tag':atm_history.address_tag,
            'type':atm_history.type,
            'order_amount':atm_history.order_amount,
            'fee':atm_history.fee,
            'discount_amount':atm_history.discount_amount,
            'discount_reason':atm_history.discount_reason,
            'actual_amount':atm_history.actual_amount,
            'status':atm_history.status,
            'error_code':atm_history.error_code,
            'error_message':atm_history.error_message,
            # 'user':atm_history.user,
            # 'balance':atm_history.balance,
            # 'refund_id':atm_history.refund_id,
            'created_at':atm_history.created_at,
            'updated_at':atm_history.updated_at,
        })


class DepositView(APIView):

    def get(self, request, *args, **kwargs):
        address = get_address('USDT',request.user.id)
        return JsonResponse({
            'address':address,
            'coin_name' : 'USDT'
        })

    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        address = get_address('USDT',user_id)
        atm_history = AtmHistoryModel()

        try:
            import time

            atm_history.blockchain = 'ETH'
            atm_history.coin_name = 'USDT'
            atm_history.txid = str(time.time())
            atm_history.address = address
            atm_history.address_tag = ''
            atm_history.type = 1
            atm_history.order_amount = 1
            atm_history.fee = 0
            atm_history.discount_amount = 0
            atm_history.actual_amount = atm_history.order_amount - atm_history.fee + atm_history.discount_amount
            atm_history.status = 'CONFIRM'
            atm_history.set_user(user_id)
            atm_history.save()
            return JsonResponse(AtmHistorySerializer(atm_history,many=False).data)
        except Exception as e:
            print(e)

        return JsonResponse()

class DepositCheckView(
                    mixins.ListModelMixin,
                    generics.GenericAPIView):
    queryset = AtmHistoryModel.objects.all()
    serializer_class = AtmHistorySerializer

    def get(self, request, *args, **kwargs):
        try:
            user_id = request.user.id
            import datetime
            now = datetime.datetime.now()
            start = now - datetime.timedelta(minutes=20, seconds=0)
            self.queryset = AtmHistoryModel.objects.filter(user_id = user_id,created_at__gt = start).order_by('-id')
        except Exception as e:
            return JsonResponse(None, HTTP_CODE_INTERNAL_SERVER_ERROR,e.args[0])

        return JsonResponse(self.list(request,args,kwargs).data)

