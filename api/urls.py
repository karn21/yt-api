from django.urls import path
from .views import VideoView

app_name = "api"

urlpatterns = [
    path("videos/", VideoView.as_view(), name="videos")
]
