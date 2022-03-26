from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('api/gallery/', views.fetch_gallery, name='fetch_gallery'),
    path('api/resources/', views.fetch_resources, name='fetch_resources'),
    path('api/team/', views.fetch_team, name='fetch_team'),
    path('api/events/',views.fetch_event,name='fetch_event'),
    path('api/committees/',views.fetch_committee,name='fetch_committee'),
    path('api/blogs/',views.fetch_blogs,name='fetch_blogs'),
    path('api/blogs/<int:pk>/',views.fetch_blog,name='fetch_blog'),
    path('api/about/',views.fetch_about,name='fetch_about'),
    path('api/token/', views.post_token, name='post_token'),
    path('api/notifications/',views.fetch_notifications,name='fetch_notifications'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
