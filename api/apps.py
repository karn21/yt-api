from django.apps import AppConfig


class ApiConfig(AppConfig):
  name = 'api'

  def ready(self):
    from .views import fetch_videos
    fetch_videos(repeat=3600)

