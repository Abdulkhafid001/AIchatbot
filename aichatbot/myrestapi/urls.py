from django.urls import path

from myrestapi import views
urlpatterns = [
    path("snippets/", views.snippet_list, name=""),
    path("snippets/<int:pk>/", views.snippet_detail, name="")
]
