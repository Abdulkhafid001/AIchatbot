from django.urls import path

from aichatweb import views


urlpatterns = [
    path('', views.homepage)
]
