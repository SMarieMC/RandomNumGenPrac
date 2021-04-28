from django.urls import path   
from . import views

urlpatterns=[
    # path('', views.index),
    path('rannum', views.rannum),
    path('reset', views.reset),
]