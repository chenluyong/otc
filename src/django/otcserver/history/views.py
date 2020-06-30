from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.
from history.models import Info as History
from history.serializers import HistoryDetailSerializer
from utils.json_response import JsonResponse





class HistoryDetail(mixins.ListModelMixin,
                  # mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = History.objects.all()
    serializer_class = HistoryDetailSerializer
    # lookup_field = 'user_id'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        self.queryset = History.objects.all().filter(user_id = user_id)
        return JsonResponse(self.list(request, *args, **kwargs).data)
