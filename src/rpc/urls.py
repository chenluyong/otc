from django.conf.urls import url,re_path
# from rest_framework.urlpatterns import format_suffix_patterns

from rpc import views


urlpatterns = [
    # rpc接口
    url(r'^$', views.Test.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)