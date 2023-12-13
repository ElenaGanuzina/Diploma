from django.shortcuts import render, get_object_or_404, redirect

from . import models, forms
from .models import Place, Route, Comment


def index(request):
    places = Place.objects.filter(pk__lte=7)
    context = {"places": places}
    return render(request, 'main.html', context)


def about(request):
    return render(request, 'about.html')


def get_all_places(request):
    places = Place.objects.all()
    context = {"places": places}
    return render(request, 'get_places.html', context)


def get_all_routes(request):
    routes = Route.objects.all()
    context = {"routes": routes}
    return render(request, 'get_routes.html', context)


def get_place(request, place_slug):
    place = get_object_or_404(Place, slug=place_slug)
    context = {'place': place}
    return render(request, 'place.html', context)


def get_route(request, route_slug):
    route = get_object_or_404(Route, slug=route_slug)
    context = {'route': route}
    return render(request, 'route.html', context)


def get_all_comments(request):
    context = dict()
    context['comments'] = Comment.objects.all()
    return render(request, 'get_comments.html', context)


def add_comment(request):
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = models.Comment(name=form.cleaned_data['name'],
                                     content=form.cleaned_data['content'])
            comment.save()

            return redirect('index')
    else:
        form = forms.CommentForm()
    return render(request, 'add_comment.html',
                  {'form': form})


# def get_routes_by_duration(request, duration: int):
#     context = dict()
#     context['routes'] = Route.objects.filter(duration=duration)
#     return render(request, 'get_routes.html', context)
#
#
# def get_routes_by_start(request, start: str):
#     context = dict()
#     context['routes'] = Route.objects.filter(start=start)
#     return render(request, 'get_routes.html', context)

#
# def login(request):
#     return render(request, 'login.html')

