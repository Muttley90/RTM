from django.contrib import admin
from django.conf.urls import url, include
from RTML_app import views
import re

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'Get/', views.getTable, name="getTable")
    ]
