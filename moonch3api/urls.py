from django.contrib import admin
from django.urls import path ,include ,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from moonch3api.views import (
    HomeSweetHome,
    SystemInfo ,
    Dev,
    Version,
    UserInfo,

)

urlpatterns = [
    path('' , HomeSweetHome.as_view() , name='Homeapi'),
    path('sys/' , SystemInfo.dataSystem , name='sys' ) ,
    path('dev/' , Dev.as_view() ),
    path('ver/' , Version.as_view() , ),


    path('info/' , UserInfo.as_view() , name='info') ,
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})
]  +   static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)