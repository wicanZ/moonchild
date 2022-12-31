
from django.contrib import admin
from django.urls import path ,include ,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from moonweb.eventpy.viewevents import ListEvent, deleteEvent, editEvent, likeEvent, makeEvent, viewEvent

from . import views
from .views import (
    UserAuthen
)

from moonweb.eventpy import *



urlpatterns = [
    path('dash/' , views.dashboard , name='dash') ,
    path('' , views.Home , name='Home'),
    path('hom/', views.sayhi, name='home'),
    path('kamra/<uuid:id>/callmeroom/', views.kamra,name='kamra'),
    path('create/', views.create ,name='create'),
    path('edit/<uuid:id>/',views.edit, name='edit'),
    path('uploadphoto/<str:id>/' , views.addnotePhoto , name='uploadnoteimg' ) , # add note image 
    path('notesetting/<str:id>/' , views.noteSetting , name='notesetting'),
    path('delete/<uuid:id>/', views.deleteNote,name='delete'),
    path('register/', views.register,name='register'),
    path('login/', views.loginMe,name='login'),
    path('logout/', views.logoutMe,name='logout'),
    path('profile/', views.profile ,name='userprofile'),
    path('deactivate' , views.deactivate , name='deactivate') ,
    path('myprofile/' , views.viewProfile , name='vpro' ) ,
    path('pro/<str:id>/' , UserAuthen.as_view() , name='prof') ,
    path('deactivateset' , views.deactivate , name='deactivatesetting') , # remove from setting 
    path('deactivate/' , views.deactivateUser , name='deactivate'),
    path('detail/<str:tle>/', views.detail , name='detail'),
    path('about/' , views.about , name='about') ,
    path('like/<uuid:pk>/' , views.Like , name="like") ,
    path('unlike/<uuid:pk>/' , views.unLike , name="unlike") ,
    path('blog/', views.addBlog , name="create-blog") ,
    path('blog/all/' , views.listBlog , name='allblog') ,
    path('blog/editblog/<uuid:id>', views.editBlog , name="edit-blog") ,
    path('blog/<uuid:pk>/', views.viewBlog , name="view-blog") ,
    path('blog/<uuid:pk>/', views.LikeBlog , name="like-blog") ,
    path('blog/editmessage/<str:id>/', views.editmessage , name='editmess' ) , 
    path('blog/delmess/<str:id>/' , views.deleteMessage , name='delmess') , 
    path('setting/user/okok/', views.Setting , name="setting") ,
    path('setting/user/okok/priv', views.Private , name="priv") ,
    path('setting/user/okok/viewpriv/<uuid:id>/', views.viewPrivate , name="viewpriv") ,
    #path('register/', CreateUser.as_view() , name='register'),
    #path('login/', LoginView.as_view() , name='login'),

    path('contact/' , views.contactus , name='contactus'),




    # event start from here

    path('event/createevent/' , makeEvent , name='createevent' ) ,
    path('event/homeevent/' , ListEvent , name='homeevent' ) ,
    path('event/<str:id>/viewevent/' , viewEvent , name='viewevent' ) ,
    path('event/<str:id>/deleteevent/' , deleteEvent , name='deleteevent' ) ,
    path('event/<str:id>/likeevent/' , likeEvent , name='likeevent' ) ,
    path('event/<str:id>/editevent/' , editEvent , name='editevent' ) ,
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})
]  +   static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

