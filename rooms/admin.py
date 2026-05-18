from django.contrib import admin
from .models import Room, Amenity
from common.admin import CommonAdmin


@admin.register(Room)
class RoomAdmin(CommonAdmin):
    list_display = (
        "name",
        "price",
        "kind",
        "owner",
        "format_created_at",
        "format_updated_at",
    )
    list_filter = (
        "country",
        "city",
        "price",
        "rooms",
        "toilets",
        "pet_friendly",
        "kind",
        "amenities",
    )


@admin.register(Amenity)
class AmenityAdmin(CommonAdmin):
    list_display = (
        "name",
        "format_created_at",
        "format_updated_at",
    )
