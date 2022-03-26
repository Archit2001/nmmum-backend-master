from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import FirebaseToken, Gallery,About, Notifications,Team,Committee,Resource,Event,Blog
from api import models
import hashlib


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model=Gallery
        fields='__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model=About
        fields='__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields='__all__'


class CommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Committee
        fields="__all__"


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resource
        fields='__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields='__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'


class FirebaseTokenSerializer(serializers.Serializer):
    token1 = serializers.CharField(max_length=256)
    token2 = serializers.CharField(max_length=256)

    def validate(self, attrs):
        token1 = attrs['token1']
        token2 = attrs['token2']
        hashed_token = hashlib.sha256(str(attrs['token1']).encode('utf-8')).hexdigest()
        
        if token2 == hashed_token:
            # self.token = token1
            return {'token': token1}
        else:
            raise serializers.ValidationError('x')

    def save(self, token):
        firebase_token = FirebaseToken(token=token)
        firebase_token.save()


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'




# class GallerySerializer(serializers.Serializer):
#     image = serializers.ImageField()
#     year = serializers.IntegerField()
#     created_at = serializers.DateTimeField(auto_now_add=True)
#     updated_at = serializers.DateTimeField()

# class ResourceSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     link = serializers.URLField(max_length=200)
#     resource_type = serializers.CharField(max_length=3, choices=ResourceTypes.choices, default=ResourceTypes.PDF)
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()

# class TeamSerializer(serializers.Serializer):
#     image = serializers.ImageField()
#     name = serializers.CharField(max_length=100)
#     info=serializers.TextField()
#     position=serializers.CharField(max_length=3, choices=TeamTypes.choices)
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()

# class EventSerializer(serializers.Serializer):
#     info = serializers.TextField(max_length=300)
#     publish_at = serializers.DateTimeField()
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()

# class CommitteeSerializer(serializers.Serializer):
#     image = serializers.ImageField()
#     info = serializers.TextField()
#     name = serializers.CharField(max_length=100)
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()

# class BlogSerializers(serializers.Serializers):
#     name= serializers.CharField(max_length=100)
#     image_cover = serializers.ImageField()
#     content = serializers.TextField()
#     published_at = serializers.DateTimeField()
#     published = serializers.BooleanField(default=False) 
#     created_at = serializers.DateTimeField()
#     updated_at =serializers.DateTimeField()

# class AboutSerializers(serializers.Serial):
#     name= serializers.CharField(max_length=50)
#     image = serializers.ImageField()
#     content = serializers.TextField()
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()


