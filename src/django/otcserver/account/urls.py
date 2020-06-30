from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from account import views

urlpatterns = [
    url(r'^$', views.Account.as_view()),

    url(r'^otc/$', views.OtcAccountList.as_view()),

    url(r'^otc/(?P<pk>[0-9]+)/$', views.OtcAccountDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)