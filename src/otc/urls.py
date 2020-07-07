from django.conf.urls import url,re_path
# from rest_framework.urlpatterns import format_suffix_patterns

from otc import views


urlpatterns = [
    # 市场订单：查询
    url(r'^market/$', views.Test.as_view()),
    url(r'^market/buy/(?P<currency>([A-Z]{0,4}))/$', views.Test.as_view()),
    url(r'^market/sell/(?P<currency>([A-Z]{0,4}))/(?P<payment_method>([A-Z]{0,4}))/$', views.Test.as_view()),
    url(r'^market/buy/(?P<currency>([A-Z]{0,4}))/$', views.Test.as_view()),
    url(r'^market/buy/(?P<currency>([A-Z]{0,4}))/(?P<payment_method>([A-Z]{0,4}))/$', views.Test.as_view()),

    # 市场订单详情：查询、下单、
    url(r'^market/(?P<market_id>([0-9]{0,32}))/$', views.Test.as_view()),

    # 订单记录
    url(r'history/',views.Test.as_view()),
    # 订单查询、修改
    url(r'history/(?P<order_id>([0-9]{0,32}))/', views.Test.as_view()),
    # 订单取消
    url(r'history/(?P<order_id>([0-9]{0,32}))/cancel/', views.Test.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)