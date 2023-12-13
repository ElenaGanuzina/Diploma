from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.urls import reverse


class Place(models.Model):
    place_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField()
    image = models.ImageField(upload_to='image/', null=True)

    def __str__(self):
        return f'{self.place_name}'

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def get_absolute_url(self):
        return reverse('get_place', kwargs={'place_slug': self.slug})


class Start(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    name = models.CharField(max_length=100, default=None)
    content = models.TextField()
    publish_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.publish_date}'


class Route(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    image = models.ImageField(upload_to='image/route/', null=True)
    description = models.TextField()
    duration = models.IntegerField()
    start = models.ForeignKey(Start, on_delete=models.CASCADE)
    places = models.ManyToManyField(Place)
    #comments = models.ForeignKey(Comment, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.name}'

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def get_absolute_url(self):
        return reverse('get_route', kwargs={'route_slug': self.slug})


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    register_date = models.DateField(auto_now=True)
    is_auth = models.BooleanField(default=False)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    def set_password(self, password):
        self.password = make_password(password)

    def check_password(self, password):
        return check_password(password, self.password)

    def __str__(self):
        return f'{self.username} {self.register_date}'



