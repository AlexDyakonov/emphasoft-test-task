from django.conf import settings
from django.db import models
from django.db.models import Q


class Room(models.Model):
    number = models.CharField(max_length=50)
    cost_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()

    def is_available(self, start_date, end_date):
        overlapping_reservations = self.reservations.filter(
            Q(start_date__lte=end_date)
            & Q(end_date__gte=start_date)
            & Q(status=Reservation.Status.ACTIVE)
        ).exists()
        return not overlapping_reservations

    def __str__(self):
        return self.number


class Reservation(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        CANCELLED = "cancelled", "Cancelled"
        COMPLETED = "completed", "Completed"

    room = models.ForeignKey(
        Room, related_name="reservations", on_delete=models.CASCADE
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.ACTIVE
    )
