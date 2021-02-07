from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from .models import Page, Content, Text, Audio, Video, Photo
from .serializers import PageSerializer, PageShortSerializer

client = Client()


class AnimalTestCase(TestCase):
    def setUp(self):
        page1 = Page.objects.create(
            title="Kuber",
            order_number=1
        )
        text = Text.objects.create(text='Lorem ipsum')
        audio = Audio.objects.create(audio='media/pages/audio/eralash.wav')
        video = Video.objects.create(video='https://youtu.be/p3_MzcZbcoI?list=PLqVZIPeC5H0lzOq9_Sqk3ya0EThOVh6uw')
        photo = Photo.objects.create(photo='media/pages/photo/test.jpg')
        Content.objects.create(
            title="Details about Kuber",
            order_number=1,
            content_type=Content.TYPE_CHOICES[0][0],
            page=page1,
            text=text
        )
        Content.objects.create(
            title="Details about Kuber",
            order_number=2,
            content_type=Content.TYPE_CHOICES[1][0],
            page=page1,
            audio=audio
        )
        Content.objects.create(
            title="Details about Kuber",
            order_number=2,
            content_type=Content.TYPE_CHOICES[1][0],
            page=page1,
            video=video
        )
        Content.objects.create(
            title="Details about Kuber",
            order_number=2,
            content_type=Content.TYPE_CHOICES[1][0],
            page=page1,
            photo=photo
        )

        text_hidden = Text.objects.create(text='Lorem ipsum')
        page_hidden = Page.objects.create(name="Docker", order_number=2, hide=True)
        Content.objects.create(
            title="Hidden content",
            order_number=1,
            content_type=Content.DICT_TYPE_CHOICES[0][0],
            page=page_hidden,
            text=text_hidden
        )

    def test_pages_list_api(self):
        response = client.get(reverse('page-list'))
        pages = Page.objects.filter(hide=False)
        serializer = PageShortSerializer(pages, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pages_detail_api(self):
        page = Page.objects.filter(hide=False).first()
        response = client.get(reverse('page-detail'), kwargs={'pk': page.pk})
        serializer = PageSerializer(page, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_hidden_pages_detail_api(self):
        page = Page.objects.filter(hide=True).first()
        response = client.get(reverse('page-detail'), kwargs={'pk': page.pk})
        serializer = PageSerializer(page, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
