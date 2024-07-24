from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    # app url config
    path('aichat/', include('aichatweb.urls')),
    # django rest framework app endpoint
    path('snippetsapi/', include('myrestapi.urls')),
    # Blog API path
    path("", include('blog.urls')) 
] + debug_toolbar_urls()
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
