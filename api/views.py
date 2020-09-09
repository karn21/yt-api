from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import Video
from background_task import background


def home(request):
  return HttpResponse("Videos fetched")

# fetch yt videos view
@background()
def fetch_videos():
  print("started")
  video = Video.objects.first()
  url = "https://www.googleapis.com/youtube/v3/search"
  params = {
    'part':"snippet",
    'maxResults':10,
    'q':"cricket",
    'type':'video',
    'order':'date',
    'publishedAfter':video.publish_timestamp.isoformat('T'),
    'key':'AIzaSyCJyQbtofvZzGavHKm0Zbc89rwxtx-g4FE'
  }
  r = requests.get(url,params=params)
  data = r.json()
  # save each video
  for video in data['items']:
    create_video(video)
  print("done")


# save to database
def create_video(video):
  # extract data from response
  video_id = video['id']['videoId']
  data = video['snippet']
  timestamp = data['publishedAt']
  title = data['title']
  description = data['description']
  thumbnail = data['thumbnails']['medium']['url']
  
  # check if video already exists
  video = Video.objects.filter(video_id = video_id)
  if not video:
    # create new video object
    Video.objects.create(title=title,description=description,publish_timestamp=timestamp,video_id=video_id,thumbnail_url=thumbnail)




