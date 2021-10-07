from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.index, name='index'),
    path('add', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    ]
