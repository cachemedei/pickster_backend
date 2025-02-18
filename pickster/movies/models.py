from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Movie(models.Model):  
    movie_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    year = models.IntegerField()
    image = models.URLField()
    status = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'movie_id', 'status')
