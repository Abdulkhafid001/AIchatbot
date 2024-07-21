from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # app url config
    path('', include('aichatweb.urls'))
]
