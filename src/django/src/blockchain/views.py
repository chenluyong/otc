
from rest_framework.views import APIView
from utils.json_response import JsonResponse
from blockchain.coins.bitcoin import BitcoinExplorer,esplora
from blockchain.coins.ethereum import ETHExplorer



class BTCAddressView(APIView):
    def get(self, request, address, format=None):
        real_time = request.GET.get('real-time')

        b = BitcoinExplorer(address)

        try:
            data = b.info(real_time)
        except Exception:
            return JsonResponse({}, 500, "Server cannot find, Please try again")

        return JsonResponse(data, 0, "success")


class ETHAddressView(APIView):
    def get(self, request, address, format=None):
        real_time = request.GET.get('real-time')

        b = ETHExplorer()

        try:
            data = b.call('address',address)
        except Exception:
            return JsonResponse({}, 500, "Server cannot find, Please try again")

        return JsonResponse(data, 0, "success")



class AddressUTXOView(APIView):
    def get(self, request, address, format=None):
        real_time = request.GET.get('real-time')
        b = BitcoinExplorer(address)

        try:
            data = b.utxo(real_time)
        except Exception:
            return JsonResponse({}, 500, "Server cannot find, Please try again")

        return JsonResponse(data, 0, "success")


class ETHAddressTransactionView(APIView):
    def get(self, request, address, format=None):
        real_time = request.GET.get('real-time')
        page = request.GET.get('page',1)
        page_size = request.GET.get('size',25)
        e = ETHExplorer()

        try:
            data = e.call('txs', address, page, page_size)
        except Exception as e:
            print(e)
            return JsonResponse({}, 500, "Server cannot find, Please try again")

        return JsonResponse(data, 0, "success")




class AddressTransactionView(APIView):
    def get(self, request, address, format=None):
        real_time = request.GET.get('real-time')
        e = esplora()

        # try:
        data = e.call('txs',address)
        # except Exception:
        #     return JsonResponse({}, 500, "Server cannot find, Please try again")

        return JsonResponse(data, 0, "success")



