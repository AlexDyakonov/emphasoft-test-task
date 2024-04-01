from django.contrib import admin
from django.urls import include, path, re_path

from .views import (
    AvailableRoomsView,
    ReservationListView,
    ReserveRoomView,
    RoomListView,
)

urlpatterns = [
    path("reservations/", ReservationListView.as_view(), name="reservations"),
    path("reserve/", ReserveRoomView.as_view(), name="reserve-room"),
    path("", RoomListView.as_view(), name="rooms"),
    path("available/", AvailableRoomsView.as_view(), name="available-rooms"),
]
