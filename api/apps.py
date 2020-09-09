from django.apps import AppConfig


class ApiConfig(AppConfig):
  name = 'api'

  def ready(self):
    from .views import fetch_videos
    from background_task.models import Task
    tasks = Task.objects.all()
    for task in tasks:
      tasks.delete()
    fetch_videos(repeat=3600)

