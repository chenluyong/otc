from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from balance import views

urlpatterns = [

    # 获取概要交易记录
    url(r'^history/$', views.BalanceHistoryListView.as_view(),name='balance_history'),
    # 通过交易记录查订单详情
    url(r'^history/(?P<history_id>(\d{1,32}))$', views.BalanceHistoryDetailView.as_view(),name='balance_history_detail'),

    # 获取特定币种余额
    url(r'^(?P<coin_name>([a-zA-Z]{3,4}))$', views.BalanceDetailView.as_view(),name='balance'),
]

urlpatterns = format_suffix_patterns(urlpatterns)