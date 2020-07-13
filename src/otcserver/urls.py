"""otcserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# coreapi
# from rest_framework.documentation import include_docs_urls

from jsonrpc.backend.django import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('balance/', include('balance.urls'),  name='balance'),
    # path('atm/', include('atm.urls'), name='atm'),
    # path('otc/', include('otc.urls'), name='otc'),
    path('jsonrpc/', include(api.urls)),
    # coreapi
    # path("api-docs/", include_docs_urls("API文档")),
]
