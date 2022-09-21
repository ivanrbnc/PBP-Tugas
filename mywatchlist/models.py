from django.db import models

# Create your models here.
class WatchlistItem(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.CharField(max_length = 150)