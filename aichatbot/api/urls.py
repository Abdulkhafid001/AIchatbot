from django.urls import path
from . import views

urlpatterns = [
    path("getname", views.get_data)
]
