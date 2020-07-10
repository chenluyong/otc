from django.shortcuts import render

from rest_framework.views import APIView

# Create your views here.
from utils import JsonResponse

class Test(APIView):

    def get(self, request, *args, **kwargs):
        print(request.GET)
        print('args:',args)
        print('kwargs:',kwargs)
        return JsonResponse({})