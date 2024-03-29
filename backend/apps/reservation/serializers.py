from rest_framework import serializers

from .models import Reservation, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

    def validate_room(self, value):
        if value.is_reserved:
            raise serializers.ValidationError("Эта комната уже зарезервирована.")
        return value


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
