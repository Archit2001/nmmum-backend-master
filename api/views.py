# from django.shortcuts import render
from django.utils import timezone
from .forms import GalleryForm
from django.http.response import JsonResponse
from . import serializers
from rest_framework.decorators import api_view
from .models import About, Blog, Committee, Event, Gallery, Notifications, Resource, Team
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def fetch_gallery(request):
    if request.method == 'GET':
        query_set=0
        form = GalleryForm(request.GET)
        if form.is_valid():
            if form.cleaned_data.get('at_home')==True:
                query_set = Gallery.objects.filter(at_home=True)
        else:
            query_set = Gallery.objects.all()
        serializer = serializers.GallerySerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)


def fetch_resources(request):
    if request.method == 'GET':
        query_set = Resource.objects.all()
        serializer = serializers.ResourceSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)


def fetch_team(request):
    if request.method == 'GET':
        query_set = Team.objects.all()
        serializer = serializers.TeamSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)


def fetch_event(request):
    if request.method == 'GET':
        query_set = Event.objects.all()
        serializer = serializers.EventSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

def fetch_committee(request):
    if request.method == 'GET':
        query_set = Committee.objects.all()
        serializer = serializers.CommitteeSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)


def fetch_blogs(request):
     if request.method == 'GET':
         query_set = Blog.objects.all().filter(published=True)
         serializer = serializers.BlogSerializer(query_set, many=True)
         return JsonResponse(serializer.data, safe=False)


def fetch_blog(request, pk):
    if request.method == 'GET':
         query_set = Blog.objects.get(pk=pk)
         serializer = serializers.BlogSerializer(query_set)
         return JsonResponse(serializer.data, safe=False)


def fetch_about(request):
    if request.method == 'GET':
        query_set = About.objects.all()
        serializer = serializers.AboutSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def post_token(request):
    if request.method == 'POST':
        serializer = serializers.FirebaseTokenSerializer(data=request.data)    

        if serializer.is_valid():
            serializer.save(serializer.validated_data['token'])

        response_obj = {'status': 201, 'message': 'success'}
        return JsonResponse(response_obj)


def fetch_notifications(request):
    if request.method == 'GET':
        query_set = Notifications.objects.filter(trigger_at__lt=timezone.now())
        serializer = serializers.NotificationSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)


# def fetch_notifications(request):
#      if request.method == 'GET':
#         query_set=0
#         form = NotificationsForm(request.GET)
#         if form.is_valid():
#             if form.cleaned_data.get('time'):
#                 query_set = Notifications.objects.filter(trigger_at__lt=form.cleaned_data.get('time'))
#         else:
#             query_set = Notifications.objects.all()
#         serializer = serializers.NotificationSerializer(query_set, many=True)
#         return JsonResponse(serializer.data, safe=False)
    

