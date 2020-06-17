from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from blockchain import views

urlpatterns = [
    url(r'^address/(?P<address>\w+)/$', views.AddressView.as_view()),
    url(r'^address/(?P<address>\w+)/utxo/$', views.AddressUTXOView.as_view()),
    url(r'^address/(?P<address>\w+)/tx/$', views.AddressTransactionView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)