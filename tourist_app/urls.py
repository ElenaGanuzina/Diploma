from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('places/', views.get_all_places, name='places'),
    path('routes/', views.get_all_routes, name='routes'),
    path('comments/', views.get_all_comments, name='comments'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('places/<slug:place_slug>/', views.get_place, name='get_place'),
    path('routes/<slug:route_slug>/', views.get_route, name='get_route'),

]
