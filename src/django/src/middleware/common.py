from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response
from utils import version
class CommonMiddleware(MiddlewareMixin):

    def process_view(self, request, callback, callback_args, callback_kwargs):
        # print("-" * 80)
        # print("MD2 中的process_view")
        # callback()
        # view_func(view_args,view_kwargs)
        pass


    def process_response(self,request,response):
        #
        # code = 0
        # if response.status_code != 200:
        #     code = response.status_code
        # # configparser.
        #
        # res = {
        #     "code" : code,
        #     "version" : version.get_version(),
        #     "data" : response.data
        # }
        # print(Response(res))
        # response.data = res
        # response.set_data()
        # return response
        pass