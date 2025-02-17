from django.db import models
from django.conf import settings

class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    year = models.IntegerField()
    image = models.URLField()

    def __str__(self):
        return self.title
    
class MovieStatus(models.Model):
    STATUS_CHOICES = [
        ('watch_later', 'Watch Later'),
        ('seen_it', 'Seen It'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)