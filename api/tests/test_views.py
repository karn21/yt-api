from django.test import TestCase
from ..models import Video
from rest_framework.test import APIClient
from rest_framework import status
from django.shortcuts import reverse
from ..serializers import VideoSerializer
from ..views import fetch_videos


class TestBackgroundTask(TestCase):
    # test video fetch when db is empty
    def test_fetch_video(self):
        check = fetch_videos.now()
        self.assertTrue(check)

    # test video fetch when db is not empty

    def test_fetch_existing(self):
        Video.objects.create(title="Title", description="New Description",
                             publish_timestamp="2020-09-09T05:05:24Z",
                             video_id="ghSvLOO0hBA",
                             thumbnail_url="https://i.ytimg.com/vi/X2kchnbIaIk/mqdefault.jpg")
        check = fetch_videos.now()
        self.assertTrue(check)


class GetVideoTestCase(TestCase):

    # setup db for test
    def setUp(self):
        self.client = APIClient()
        Video.objects.create(title="Title", description="New Description",
                             publish_timestamp="2020-09-09T05:05:24Z",
                             video_id="ghSvLOO0hBA",
                             thumbnail_url="https://i.ytimg.com/vi/X2kchnbIaIk/mqdefault.jpg")
        Video.objects.create(title="Title 2", description="New Video Description",
                             publish_timestamp="2020-09-09T05:04:57Z",
                             video_id="ghSvLOO0hBA",
                             thumbnail_url="https://i.ytimg.com/vi/X2kchnbIaIk/mqdefault.jpg")
        Video.objects.create(title="Title 3", description="New Description for video",
                             publish_timestamp="2020-09-09T04:52:34Z",
                             video_id="ghSvLOO0hBA",
                             thumbnail_url="https://i.ytimg.com/vi/X2kchnbIaIk/mqdefault.jpg")

    # test for get all content
    def test_get_all_content(self):
        response = self.client.get(reverse('api:videos'))
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test for get search content
    def test_get_search_content(self):
        response = self.client.get("%s?search=title" %
                                   reverse('api:videos'))
        videos = Video.objects.filter(title__contains="title")
        serializer = VideoSerializer(videos, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
