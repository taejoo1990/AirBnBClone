from django.contrib import admin
from .models import Room, Amenity
from common.admin import CommonAdmin


@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(CommonAdmin):

    actions = (reset_prices,)
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        # "owner",
        "rating",
        "format_created_at",
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

    search_fields = ("owner__username",)


@admin.register(Amenity)
class AmenityAdmin(CommonAdmin):
    list_display = (
        "name",
        "format_created_at",
        "format_updated_at",
    )
