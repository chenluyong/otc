from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from blockchain import views

urlpatterns = [
    # 比特币正则 (^[13][a-km-zA-HJ-NP-Z0-9]{26,33}$)|(^bc[a-z0-9]{40,80}$)
    # 以太坊正则 ^(0x)?[0-9a-fA-F]{40}$
    url(r'^address/(?P<address>([13][a-km-zA-HJ-NP-Z0-9]{26,33}))/$', views.BTCAddressView.as_view()),
    url(r'^address/(?P<address>(bc[a-z0-9]{40,80}))/$', views.BTCAddressView.as_view()),
    url(r'^address/(?P<address>(0x[a-z0-9]{40,40}))/$', views.ETHAddressView.as_view()),

    url(r'^address/(?P<address>([13][a-km-zA-HJ-NP-Z0-9]{26,33}))/utxo/$', views.AddressUTXOView.as_view()),
    url(r'^address/(?P<address>(bc[a-z0-9]{40,80}))/utxo/$', views.BTCAddressView.as_view()),


    url(r'^address/(?P<address>([13][a-km-zA-HJ-NP-Z0-9]{26,33}))/tx/$', views.AddressTransactionView.as_view()),
    url(r'^address/(?P<address>(0x[a-z0-9]{40,40}))/tx/$', views.ETHAddressTransactionView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)