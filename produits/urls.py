from django.urls import path
from django.urls import include
from produits import admin
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
    path('result/<int:number>', views.result, name='result'),
]