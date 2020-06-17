from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ip import views

urlpatterns = [
    url(r'^search/(?P<ip>((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3})/$', views.IpMaps.as_view()),
    url(r'^search/myip/$', views.MyIpMaps.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)