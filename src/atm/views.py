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
        return JsonResponse(self.list(request, *args, **kwargs).data)


class AtmHistoryDetailView(APIView):


    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        atm_id = int(kwargs['atm_id'])
        if user_id is None:
            return JsonResponse(None, HTTP_CODE_UNAUTHORIZED)

        atm_history = AtmHistoryModel.objects.get(user_id=user_id, id=atm_id)

        print(atm_history)
        # return JsonResponse(atm_history)
        return JsonResponse()
