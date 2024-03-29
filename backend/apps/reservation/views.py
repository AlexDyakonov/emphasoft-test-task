from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from .filters import RoomFilter
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
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoomFilter

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return super().get_permissions()
