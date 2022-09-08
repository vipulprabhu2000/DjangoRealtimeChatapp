from django.urls import path
from . import views

urlpatterns=[
path('',views.home,name='home'),
path('checkview',views.checkview,name='checkview'),
path('<str:Roomname>/',views.Room,name='Room'),
path('send',views.send,name='send'),
path('getmessages/<str:Roomname>/',views.getmessages,name='getmessages'),
]