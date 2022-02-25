from django.contrib import admin
from django.urls import path, include

from apps.core.views import about, config, home

urlpatterns = [
    path('', home),
    path('about', about),
    path('config', config),
]
