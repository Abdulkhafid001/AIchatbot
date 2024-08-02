from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from myrestapi import views
from rest_framework import renderers
from myrestapi.views import SnippetViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
# api_root = SnippetViewSet.as_view({
#     'get': 'list'
# })

# API endpoints
urlpatterns = format_suffix_patterns([
    path("snippets/", snippet_list, name='snippet-list'),
    path("snippets/<int:pk>/", snippet_detail, name="snippet-detail"),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    # path('', views.api_root),
    path('snippets/<int:pk>/highlight/',
         snippet_highlight, name='snippet-highlight'),
])


# append a set of format_suffix_patterns in addition to the existing URLs.
urlpatterns = format_suffix_patterns(urlpatterns)

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
