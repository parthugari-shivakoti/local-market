from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('index.html', views.index, name = 'index'),
    path('shop.html', views.shop, name = 'shop'),
    path('contact.html', views.contact, name = 'contact'),
    
]