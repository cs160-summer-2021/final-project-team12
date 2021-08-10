# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plan/', views.plan, name='plan'),
    path('view/', views.view, name='view'),
    path('explore/', views.explore, name='explore'),

]
