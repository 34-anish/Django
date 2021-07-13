# Here I will be writing all the urls for linking with my project
from django.contrib import admin
from django.urls import path
from practice_app import views

urlpatterns = [
    path('', views.index,name='index'),
    path('index',views.index ,name ='index'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
]
