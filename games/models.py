from django.db import models

# Create your models here.
class Game(models.Model):
    STATUS_CHOICES = {
        ('W', 'Wishlist'),
        ('P', 'Playing'),
        ('C', 'Completed'),
        ('D', 'Dropped'),
    }

    name = models.CharField(max_length=255)
    platform = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
