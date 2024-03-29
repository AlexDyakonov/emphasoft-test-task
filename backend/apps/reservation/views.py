from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from .models import Reservation, Room
from .serializers import ReservationSerializer, RoomSerializer


class ReservationListView(generics.ListAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Reservation.objects.all()
        return Reservation.objects.filter(user=self.request.user)


class RoomListView(generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return super().get_permissions()
