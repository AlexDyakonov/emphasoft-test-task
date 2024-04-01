from django import forms
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Reservation, Room


class ReservationInline(admin.TabularInline):
    model = Reservation
    extra = 1
    fields = ["user", "start_date", "end_date"]


class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "cost_per_night",
        "capacity",
    )
    search_fields = ("number",)
    list_filter = ("capacity",)
    inlines = [
        ReservationInline,
    ]


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "cost_per_night",
        "capacity",
    )
    search_fields = ("number",)
    list_filter = ("capacity",)
    inlines = [
        ReservationInline,
    ]


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "room",
        "user",
        "start_date",
        "end_date",
    )
    list_filter = (
        "start_date",
        "end_date",
    )
    search_fields = (
        "room__number",
        "user__username",
    )
    ordering = ("-start_date",)

    def room_link(self, obj):
        link = reverse("admin:reservation_room_change", args=[obj.room.id])
        return format_html('<a href="{}">{}</a>', link, obj.room.number)

    room_link.short_description = "Room"
