
from django.contrib import admin
from django.urls import path ,include ,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from .views import HomeBlog

urlpatterns = [
    path('' , HomeBlog , name='Home'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})
]  +   static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

