from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='homepage'),
    # path('is_intru',views.get_intrusion,name='is_intruded'),
]
