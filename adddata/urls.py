
#coding=utf-8
from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$',views.zhuye,name = 'zhuye'),
    url(r'^website/(?P<question_id>\w+)',views.listroom,name = 'listroom'),
]