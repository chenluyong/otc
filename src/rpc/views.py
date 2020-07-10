from django.shortcuts import redirect,reverse
import json

from rest_framework.views import APIView

# Create your views here.
from utils import JsonResponse

class Test(APIView):
    # def get(self, request, *args, **kwargs):
    #     print(request.POST.get('method'))
    #
    #     try:
    #         return redirect(reverse('account_detail', kwargs={'pk': 1}))
    #     except Exception as e:
    #         print(e)
    #
    #     return JsonResponse()

    def post(self, request, *args, **kwargs):
        request_json = json.loads(request.body)
        method = request_json.get('method')
        params = request_json.get('params')

        try:
            resp = reverse(method, args=params)
            return redirect(resp)
        except Exception as e:
            print(e)
        return JsonResponse(msg='not find')
