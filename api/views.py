import requests
from .models import Video
from background_task import background
from rest_framework import generics
from .serializers import VideoSerializer
from django.db.models import Q

# Background Views

# fetch yt videos view


@background()
def fetch_videos():
    print("started")
    # get last video
    video = Video.objects.first()
    timestamp = ""
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': "snippet",
        'maxResults': 10,
        'q': "cricket",
        'type': 'video',
        'order': 'date',
        'key': 'AIzaSyCJyQbtofvZzGavHKm0Zbc89rwxtx-g4FE'
    }
    # if last video exists modify parameters
    if video:
        timestamp = video.publish_timestamp.isoformat('T')
        params['publishedAfter'] = timestamp
    r = requests.get(url, params=params)
    data = r.json()
    # save each video
    for video in data['items']:
        create_video(video)
    print("done")
    return True


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
    video = Video.objects.filter(video_id=video_id)
    if not video:
        # create new video object
        Video.objects.create(title=title, description=description,
                             publish_timestamp=timestamp, video_id=video_id,
                             thumbnail_url=thumbnail)


# API VIEWS

# GET API view
class VideoView(generics.ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        queryset = Video.objects.all()
        # get query string
        query = self.request.query_params.get('search', None)
        if query:
            # filter with original query string
            final_qs = queryset.filter(Q(title__icontains=query) | Q(
                description__icontains=query)).distinct()
            # split query string
            query = query.split(" ")
            # search with each query string
            for q in query:
                qs = queryset.filter(Q(title__icontains=q) | Q(
                    description__icontains=q)).distinct()
                final_qs = (qs | final_qs).distinct()
            return final_qs
        return queryset
