import django_filters

from .models import Room


class RoomFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(
        field_name="cost_per_night", lookup_expr="gte"
    )
    max_price = django_filters.NumberFilter(
        field_name="cost_per_night", lookup_expr="lte"
    )
    min_capacity = django_filters.NumberFilter(field_name="capacity", lookup_expr="gte")
    max_capacity = django_filters.NumberFilter(field_name="capacity", lookup_expr="lte")

    class Meta:
        model = Room
        fields = ["cost_per_night", "capacity"]
