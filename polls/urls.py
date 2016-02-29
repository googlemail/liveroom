#-------------------------------------------------------------------------------
# Name:        模块2
# Purpose:
#
# Author:      Administrator
#
# Created:     21-12-2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^polls/', views.Indexview.as_view(),name = 'index'),
    url(r'^(?P<pk>[0-9]+?)$',views.Choiceview.as_view(),name = 'choice'),
    url(r'^(?P<pk>[0-9]+?)/vote$',views.Vote,name = 'vote')
]