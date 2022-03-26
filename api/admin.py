from django.contrib import admin
from django.db.models import fields
from .models import Resource, Gallery, About, Team, Event, Blog, Committee ,Notifications, FirebaseToken, Recent

# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    fields = ['image', 'url', 'year', 'at_home']
    list_display = ['admin_photo', 'url', 'year', 'created_at', 'updated_at', 'at_home']
    list_display_links = ['admin_photo']


class TeamAdmin(admin.ModelAdmin):
    fields = ['image', 'name', 'description', 'category', 'position']
    list_display = ['admin_photo', 'name', 'category', 'position', 'created_at', 'updated_at']
    list_display_links = ['admin_photo', 'name']


admin.site.register(Resource)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(About)
admin.site.register(Team, TeamAdmin)
admin.site.register(Event)
admin.site.register(Blog)
admin.site.register(Committee)
admin.site.register(Notifications)
admin.site.register(FirebaseToken)
admin.site.register(Recent)