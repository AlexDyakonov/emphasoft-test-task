from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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


class ReserveRoomView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        room_id = request.data.get("room")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        room = get_object_or_404(Room, pk=room_id)

        if room.is_available(start_date, end_date):
            return super().create(request, *args, **kwargs)
        else:
            return Response(
                {"error": "Room is not available for the given dates."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class AvailableRoomsView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get("start_date", None)
        end_date = self.request.query_params.get("end_date", None)
        if start_date and end_date:
            available_rooms = []
            for room in Room.objects.all():
                if room.is_available(start_date, end_date):
                    available_rooms.append(room)
            return available_rooms
        else:
            return Room.objects.none()

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return super().get_permissions()
