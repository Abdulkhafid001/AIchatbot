from django.urls import path
from django.template import loader

from aichatweb import views


urlpatterns = [
    path('', views.homepage)
]
