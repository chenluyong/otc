
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class IpMaps(APIView):

    def get(self, request, ip, format=None):
        res = {}

        return Response(res)