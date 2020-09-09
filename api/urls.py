from django.urls import path
from .views import home

app_name="api"

urlpatterns = [
    path("fetch/",home,name="fetch_videos")
]
