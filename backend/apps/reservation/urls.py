from django.contrib import admin
from django.urls import include, path, re_path

from .views import ReservationListView

urlpatterns = [
    path("reservations/", ReservationListView.as_view(), ""),
]
