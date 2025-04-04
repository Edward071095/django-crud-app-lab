from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    released = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} ({self.id})'

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'movie_id': self.id})
    
class Cast(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=30)
    notable_films = models.CharField(max_length=100)
    years_active = models.CharField(max_length=100)

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.name} {self.age} ({self.id})'