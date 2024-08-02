from django.urls import include, path
from blog.views import BlogList

urlpatterns = [
    path("", BlogList.as_view(), name="list-all-blog-entries")
]
