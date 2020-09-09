from django.db import models



class Video(models.Model):
  title = models.TextField()
  description = models.TextField()
  publish_timestamp = models.DateTimeField()
  video_id = models.CharField(max_length=20) # yt id of video
  thumbnail_url = models.URLField()

  def __str__(self):
    return self.title
