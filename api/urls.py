from django.urls import path
from .views import fetch_videos

app_name="api"

urlpatterns = [
    path("fetch/",fetch_videos,name="fetch_videos")
]
