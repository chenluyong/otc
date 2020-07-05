from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from atm import views

urlpatterns = [
    # 获取概要交易记录
    url(r'^history/$', views.AtmHistoryListView.as_view(),name='atm_history'),
    # 通过交易记录查订单详情
    url(r'^history/(?P<atm_id>(\d{1,32}))$', views.AtmHistoryDetailView.as_view(),name='atm_history_detail'),

    # 获取充值地址
    url(r'^deposit/$', views.DepositView.as_view()),
    # 获取新的充值地址
    # url(r'^deposit/update/$)$', views.BalanceHistoryDetailView.as_view(), name='balance_history_detail'),
    # url(r'^deposit/update/(?P<coin_name>([a-zA-Z]{3,4}))$', views.BalanceHistoryDetailView.as_view(),
    #     name='balance_history_detail'),
    # 检测到账
    url(r'^deposit/check/$', views.DepositCheckView.as_view(),),

    # 提现到目标地址
]

urlpatterns = format_suffix_patterns(urlpatterns)