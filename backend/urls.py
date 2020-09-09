from django.contrib import admin
from django.urls import path, include
from api import urls as api_urls
from .views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name="dashboard"),
    path('api/', include(api_urls, namespace="api")),
]
