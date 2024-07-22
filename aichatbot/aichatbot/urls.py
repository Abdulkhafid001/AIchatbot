from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    # app url config
    path('aichat/', include('aichatweb.urls')),
    # django rest framework app endpoint
    path('', include('myrestapi.urls')),
]
