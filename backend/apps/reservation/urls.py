from django.contrib import admin
from django.urls import include, path, re_path

from .views import ReservationListView, RoomListView

urlpatterns = [
    path("reservations/", ReservationListView.as_view(), name="reservations"),
    path("", RoomListView.as_view(), name="rooms"),
]
