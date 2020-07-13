# from django.shortcuts import render
# from django.shortcuts import redirect,reverse
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
#
# from rest_framework.views import APIView
# from rest_framework import generics
# from rest_framework import mixins
#
# # Create your views here.
#
# from balance.models import History as BalanceHistoryModel
# from balance.serializers import BalanceHistorySerializer,BalanceDetailSerializer
#
# from utils import JsonResponse
# from utils.http_code import *
#
#
#
# class BalanceHistoryListView(
#                     mixins.ListModelMixin,
#                     generics.GenericAPIView):
#
#     queryset = BalanceHistoryModel.objects.all()
#     serializer_class = BalanceHistorySerializer
#
#     @method_decorator(login_required)
#     def get(self, request, *args, **kwargs):
#         user_id = request.user.id
#         if user_id is None:
#             return JsonResponse(None, HTTP_CODE_UNAUTHORIZED)
#
#         self.queryset = BalanceHistoryModel.objects.all().filter(user_id=user_id)
#         return JsonResponse(self.list(request, *args, **kwargs).data)
#
#
# class BalanceDetailView(
#                     mixins.ListModelMixin,
#                     generics.GenericAPIView):
#
#     queryset = BalanceHistoryModel.objects.all()
#     serializer_class = BalanceDetailSerializer
#     lookup_field = 'coin_name'
#
#     @method_decorator(login_required)
#     def get(self, request, *args, **kwargs):
#         user_id = request.user.id
#         coin_name = str(kwargs['coin_name']).upper()
#         if user_id is None:
#             return JsonResponse(None, HTTP_CODE_UNAUTHORIZED)
#         self.queryset = BalanceHistoryModel.objects.all().filter(user_id=user_id,coin_name=coin_name).order_by('-id')[:1]
#         return JsonResponse(self.list(request, *args, **kwargs).data)
#
#
# class BalanceHistoryDetailView(APIView):
#
#     @method_decorator(login_required)
#     def get(self, request, *args, **kwargs):
#         history_id = int(kwargs['history_id'])
#         user_id = request.user.id
#         if user_id is None:
#             return JsonResponse(None, HTTP_CODE_UNAUTHORIZED)
#
#         try:
#             history_detail = BalanceHistoryModel.objects.get(user_id=user_id, id = history_id)
#
#             business = history_detail.business
#             order_id = history_detail.order_id
#
#         except Exception as e :
#             # print(e.args)
#             return JsonResponse(None, HTTP_CODE_NOT_FOUND,msg=e.args[0])
#
#         return JsonResponse()