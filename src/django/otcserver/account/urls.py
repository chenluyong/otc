from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from account import views

urlpatterns = [
    url(r'^$', views.Account.as_view()),
    url(r'^(?P<pk>(\d{1,32}))/$', views.AccountDetail.as_view(),name='account_detail'),
    url(r'^login/$', views.AccountLogin.as_view(), name='account_login'),

    url(r'^otc/$', views.OtcAccountList.as_view()),

    url(r'^otc/(?P<pk>(\d{1,32}))/$', views.OtcAccountDetail.as_view()),
    url(r'^otc/(?P<username>(\w+))/$', views.OtcAccountDetail.as_view()),

    url(r'^test/$', views.Test.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)