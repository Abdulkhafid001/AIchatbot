from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myrestapi import views

urlpatterns = [
    path("snippets/", views.SnippetList.as_view()),
    path("snippets/<int:pk>/", views.SnippetDetail.as_view())
]

# append a set of format_suffix_patterns in addition to the existing URLs.
urlpatterns = format_suffix_patterns(urlpatterns)
