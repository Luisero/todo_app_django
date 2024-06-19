from django.urls import path 
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('auth/singup/', views.singup, name='singup'),
    path('auth/logout/', views.logout, name='logout')
]