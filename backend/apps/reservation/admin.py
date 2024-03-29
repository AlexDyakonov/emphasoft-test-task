from django.contrib import admin

from .models import Reservation, Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "cost_per_night",
        "capacity",
    )
    search_fields = ("number",)
    list_filter = ("capacity",)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "room",
        "user",
        "is_reserved",
        "created_at",
        "ended_at",
    )
    list_filter = ("is_reserved", "created_at")
    search_fields = (
        "room__number",
        "user__username",
    )

    def user_info(self, obj):
        return obj.user.get_full_name()

    ordering = ("-created_at",)
