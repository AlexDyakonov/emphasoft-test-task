from django.contrib import admin
from django.urls import include, path, re_path

from .views import (
    AvailableRoomsView,
    ReservationCancelView,
    ReservationCreateView,
    ReservationsListView,
    RoomListView,
)

urlpatterns = [
    path("reservations/", ReservationsListView.as_view(), name="reservations"),
    path("", RoomListView.as_view(), name="rooms"),
    path("available/", AvailableRoomsView.as_view(), name="available-rooms"),
    path(
        "reservations/create/",
        ReservationCreateView.as_view(),
        name="create-reservation",
    ),
    path(
        "reservations/cancel/<int:pk>/",
        ReservationCancelView.as_view(),
        name="cancel-reservation",
    ),
]
