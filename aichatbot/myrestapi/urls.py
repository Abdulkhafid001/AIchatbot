from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from myrestapi import views
urlpatterns = [
    path("snippets/", views.snippet_list, name=""),
    path("snippets/<int:pk>/", views.snippet_detail, name="")
]

# append a set of format_suffix_patterns in addition to the existing URLs.
urlpatterns = format_suffix_patterns(urlpatterns)
