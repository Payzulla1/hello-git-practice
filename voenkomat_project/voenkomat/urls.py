from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('conscripts/', views.conscript_list, name='conscript_list'),
]