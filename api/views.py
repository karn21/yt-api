from django.shortcuts import render
import requests
from django.http import HttpResponse

# url : https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q=cricket&type=video&key=AIzaSyCJyQbtofvZzGavHKm0Zbc89rwxtx-g4FE


# fetch yt videos view
def fetch_videos(request):
  url = "https://www.googleapis.com/youtube/v3/search"
  params = {
    'part':"snippet",
    'maxResults':10,
    'q':"cricket",
    'type':'video',
    'key':'AIzaSyCJyQbtofvZzGavHKm0Zbc89rwxtx-g4FE'
  }
  r = requests.get(url,params=params)
  data = r.json()
  print(data)
  return HttpResponse("Videos fetched")
