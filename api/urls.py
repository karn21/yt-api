from django.urls import path
from .views import home,VideoView

app_name="api"

urlpatterns = [
    path("videos/",VideoView.as_view(),name="all_videos")
]
