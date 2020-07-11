from django.shortcuts import render

from rest_framework.views import APIView

# Create your views here.
from utils import JsonResponse
from jsonrpc.backend.django import api

class Test(APIView):

    def get(self, request, *args, **kwargs):
        print(request.GET)
        print('args:',args)
        print('kwargs:',kwargs)
        return JsonResponse({})


@api.dispatcher.add_method(name="my.method")
def my_method(request, *args, **kwargs):
    rsp = Test().get(request,args,kwargs)
    print(rsp.data)

    return args, kwargs,rsp.data