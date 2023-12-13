from django.contrib import admin
from .models import Place, Route, Comment, Start


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['place_name', 'description', 'image']
    search_fields = ['place_name']
    search_help_text = 'Search by place name'
    fields = ['place_name', 'description', 'image']


class RouteAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image']
    search_fields = ['duration']
    search_help_text = 'Search by duration'
    fields = ['name', 'description', 'image', 'duration', 'places', 'start']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'publish_date', 'content']
    search_fields = ['publish_date']
    search_help_text = 'Search by publishing date'
    fields = ['name', 'publish_date', 'content']


class StartAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    search_help_text = 'Search by name'
    fields = ['name']


admin.site.register(Place, PlaceAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Start, StartAdmin)

