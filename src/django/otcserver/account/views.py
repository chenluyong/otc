from django.shortcuts import redirect,reverse

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError


from account.models import Info as User
from account.serializers import OtcAccountListSerializer,OtcAccountDetailSerializer,UserDetailSerializer
from utils.json_response import JsonResponse
from utils.http_code import *


class Account(APIView):
    # 获取信息
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('account_login'))
        return redirect(reverse('account_detail', kwargs = {'pk':request.user.id}))


class AccountDetail(# mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    # 获取信息
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user_id = int(kwargs.get('pk'))
        if user_id != request.user.id:
            return JsonResponse(None,HTTP_CODE_UNAUTHORIZED)
        return JsonResponse(self.retrieve(request, *args, **kwargs).data)


# 基本账户业务
class AccountLogin(APIView):

    # 获取信息
    def get(self, request):
        return JsonResponse(code=HTTP_CODE_BAD_REQUEST)

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

                return JsonResponse(code=code)
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

            return JsonResponse(code=code)
        except IntegrityError as e:
            code = e.args[0]
            msg = e.args[1]

        return JsonResponse(None, code, msg)



# 特殊三方账户
class TelegramAccount(APIView):

    # 获取账号信息
    def get(self,request):
        pass

    # 创建账号
    def put(self,request):
        pass

# OTC账户列表
class OtcAccountList(mixins.ListModelMixin,
                  # mixins.CreateModelMixin,
                  generics.GenericAPIView):

    # 获取OTC商户列表信息
    queryset = User.objects.all()
    serializer_class = OtcAccountListSerializer

    def get(self, request, *args, **kwargs):
        return JsonResponse(self.list(request, *args, **kwargs).data)


# OTC账户详情
class OtcAccountDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                  generics.GenericAPIView):

    # 获取OTC商户详细信息
    queryset = User.objects.all()
    serializer_class = OtcAccountDetailSerializer
    # lookup_field = 'username'
    def get(self, request, *args, **kwargs):
        try:
            return JsonResponse(self.retrieve(request, *args, **kwargs).data)
        except Exception :
            return JsonResponse(None,HTTP_CODE_INTERNAL_SERVER_ERROR)


    # 修改OTC账户详情
    def post(self, request, *args, **kwargs):
        request_otc_id = int(kwargs['pk'])

        print(request_otc_id,'：',request.user.id)
        if request_otc_id != request.user.id:
            return JsonResponse({'id':request.user.id},HTTP_CODE_UNAUTHORIZED)
        return JsonResponse(self.update(request, *args, **kwargs).data)


class Test(APIView):
    def get(self,request):
        from django.contrib.auth.hashers import make_password, check_password
        pswd = make_password('asdasd','dwZ5e6fC6O6S','pbkdf2_sha256')
        b =check_password('asdasd','pbkdf2_sha256$180000$dwZ5e6fC6O6S$YmNmZDE0YjA4NmU2ZTNiN2M0NDRhZTQxMTQ5Mzk3NzkwZDk3NzM2OTc0NWQ1NDllNGQwZjAxNTViNmI0ZjFlZg==')

        # print(b)
        return JsonResponse({
            'pswd':'asdasd',
            'pswd_encode':pswd
        })