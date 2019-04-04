from django.urls import path
from django.conf.urls import re_path
from . import views


urlpatterns = [
    re_path('test1', views.fun1),
    re_path('token', views.get_token),
    re_path('', views.homepage),
]