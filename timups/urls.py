from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.index, name='index'),
    path('add', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('watchPage/', views.watchPage, name='watchPage'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name= 'cart')
    ]
