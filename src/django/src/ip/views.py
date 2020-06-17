
from rest_framework.views import APIView
from rest_framework.response import Response

from ip.utils import ip_search
import requests

class IPView(APIView):
    def get_ip(self,ip):
        pos = ip_search.search(ip)
        fields = pos.split("|")
        nation = fields[0] if fields[0] != "0" else ""
        nation_other = fields[1] if fields[1] != "0" else ""
        province = fields[2] if fields[2] != "0" else ""
        city = fields[3] if fields[3] != "0" else ""
        network = fields[4] if fields[4] != "0" else ""

        return {
            "ip" : ip,
            "nation": nation,
            "nation_other": nation_other,
            "province": province,
            "city": city,
            "network": network,
            "allow" : True,
        }


class IpMaps(IPView):

    def get(self, request, ip, format=None):
        res = self.get_ip(ip)
        return Response(res)

class MyIpMaps(IPView):

    def get(self, request, format=None):
        """
        获取ip地址
        :param request:
        :return:
        """
        ip = request.META.get("HTTP_X_FORWARDED_FOR", "")
        if not ip:
            ip = request.META.get('REMOTE_ADDR', "")
        client_ip = ip.split(",")[-1].strip() if ip else ""
        # return client_ip

        # client_ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get('HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')

        res = self.get_ip(client_ip)
        return Response(res)


class IpWeatherMaps(IPView):

    def get(self, request, ip, format=None):
        #client_ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get('HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
        res = self.get_ip(ip)
        res['weather'] = requests.get("http://flash.weather.com.cn/wmaps/xml/china.xml").text

        return Response(res)
