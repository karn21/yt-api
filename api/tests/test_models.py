from django.test import TestCase
from ..models import Video


class ModelTestCase(TestCase):

    # create video object test
    def setUp(self):
        Video.objects.create(title="Title", description="New Description",
                             publish_timestamp="2020-09-09T05:05:24Z",
                             video_id="ghSvLOO0hBA",
                             thumbnail_url="https://i.ytimg.com/vi/X2kchnbIaIk/mqdefault.jpg")

    def test_content_str(self):
        video = Video.objects.get(title="Title")
        self.assertEqual(video.video_id, "ghSvLOO0hBA")
        self.assertEqual(str(video), "Title")
