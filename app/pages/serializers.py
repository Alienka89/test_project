from rest_framework import serializers
from .models import (Page, Content, Photo, Text, Audio, Video)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('photo',)


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('video', 'subtitles')


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ('audio', 'bitrate')


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('text',)


class ContentSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(many=False, required=False)
    text = TextSerializer(many=False, required=False)
    audio = AudioSerializer(many=False, required=False)
    video = VideoSerializer(many=False, required=False)

    class Meta:
        model = Content
        fields = ('id', 'photo', 'text', 'audio', 'video', 'content_type', 'title', 'order_number', 'counter')


class PageSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True, required=True)

    class Meta:
        model = Page
        fields = ('id', 'title', 'counter', 'order_number', 'content')


class PageShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'title', 'counter', 'order_number',)
