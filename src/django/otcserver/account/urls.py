from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from account import views

urlpatterns = [
    url(r'^$', views.Account.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)