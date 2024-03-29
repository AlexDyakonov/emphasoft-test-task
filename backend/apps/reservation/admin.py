from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Reservation, Room


class ReservationInline(admin.TabularInline):
    model = Reservation
    extra = 1


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "cost_per_night",
        "capacity",
        "is_reserved",
    )
    search_fields = ("number",)
    list_filter = ("is_reserved", "capacity")
    inlines = [
        ReservationInline,
    ]


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "room_link",
        "user",
        "created_at",
        "ended_at",
    )
    list_filter = ("created_at",)
    search_fields = (
        "room__number",
        "user__username",
    )

    def room_link(self, obj):
        link = reverse("admin:reservation_room_change", args=[obj.room.id])
        return format_html('<a href="{}">{}</a>', link, obj.room.number)

    room_link.short_description = "Room"

    def user_info(self, obj):
        return obj.user.get_full_name()

    ordering = ("-created_at",)
