from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from history import views

urlpatterns = [

    url(r'^$', views.HistoryDetail.as_view()),

    # url(r'^otc/(?P<pk>(\d{1,32}))/$', views.OtcAccountDetail.as_view()),
    # url(r'^otc/(?P<username>(\w+))/$', views.OtcAccountDetail.as_view()),

    # url(r'^test/$', views.Test.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)