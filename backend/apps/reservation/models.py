from django.conf import settings
from django.db import models


class Room(models.Model):
    number = models.CharField(max_length=50)
    cost_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    is_reserved = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.number


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    ended_at = models.DateTimeField(null=True)
