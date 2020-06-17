
from rest_framework.views import APIView
from utils.json_response import JsonResponse
from blockchain.coins.bitcoin import Bitcoin



class AddressView(APIView):
    def get(self, request, address, format=None):
        real_time = request.GET.get('real-time')
        b = Bitcoin(address)
        data = b.info(real_time)
        return JsonResponse(data, 0, "success")


class AddressUTXOView(APIView):
    def get(self, request, address, format=None):
        real_time = request.GET.get('real-time')
        b = Bitcoin(address)
        data = b.utxo(real_time)
        return JsonResponse(data, 0, "success")



class AddressTransactionView(APIView):
    def get(self, request, address, format=None):
        real_time = request.GET.get('real-time')
        b = Bitcoin(address)
        data = b.transaction(real_time)
        return JsonResponse(data, 0, "success")
