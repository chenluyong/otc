from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

from django.contrib.auth import login,authenticate
from account.models import Info as User

from utils.json_response import JsonResponse


from django.db.utils import IntegrityError
from utils.http_code import *
from .serializers import AccountInfoSerializer


class Account(APIView):

    # 获取信息
    def get(self, request):
        code = HTTP_CODE_SUCCESS

        while True:
            if not request.user.is_authenticated:
                code = HTTP_CODE_UNAUTHORIZED
                break

            username = request.user.get_username()

            return JsonResponse({
                'username': username,
             }, code)

        return JsonResponse(None,code)

    # 登录
    def post(self,request):
        code = HTTP_CODE_SUCCESS
        msg = None
        try:
            while True:
                username = request.data.get('username')
                password = request.data.get('password')
                print('-' * 60)
                if not username or not password:
                    code = HTTP_CODE_BAD_REQUEST
                    break
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                else:
                    code = HTTP_CODE_INCORRECT_PASSWORD
                    break

                return JsonResponse(None, code)
        except IntegrityError as e:
            code = e.args[0]
            msg = e.args[1]

        return JsonResponse(None, code, msg)

    # 创建
    def put(self, request):
        code = HTTP_CODE_SUCCESS
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        try:
            user_obj = User.objects.create_user(username=username, password=password, email=email)
            if user_obj:
                login(request, user_obj)
            else:
                code = HTTP_CODE_FORBIDDEN

            return JsonResponse(None, code)
        except IntegrityError as e:
            code = e.args[0]
            msg = e.args[1]

        return JsonResponse(None, code, msg)




class TelegramAccount(APIView):

    # 获取账号信息
    def get(self,request):
        pass

    # 创建账号
    def put(self,request):
        pass


class OtcAccountList(mixins.ListModelMixin,
                  # mixins.CreateModelMixin,
                  generics.GenericAPIView):

    # 获取OTC商户列表信息
    queryset = User.objects.all()
    serializer_class = AccountInfoSerializer

    def get(self, request, *args, **kwargs):
        return JsonResponse(self.list(request, *args, **kwargs).data)



class OtcAccountDetail(mixins.RetrieveModelMixin,
                  generics.GenericAPIView):

    # 获取OTC商户详细信息
    queryset = User.objects.all()
    serializer_class = AccountInfoSerializer

    def get(self, request, *args, **kwargs):
        return JsonResponse(self.retrieve(request, *args, **kwargs).data)
