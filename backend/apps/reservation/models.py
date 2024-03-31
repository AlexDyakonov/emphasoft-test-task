from django.conf import settings
from django.db import models


class Room(models.Model):
    number = models.CharField(max_length=50)
    cost_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()

    def __str__(self):
        return self.number


class Reservation(models.Model):
    room = models.ForeignKey(
        Room, related_name="reservations", on_delete=models.CASCADE
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
