from django.contrib import admin
from common.admin import CommonAdmin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(CommonAdmin):
    list_display = (
        "user",
        "kind",
        "check_in",
        "check_out",
        "experience_time",
        "guests",
        "format_updated_at",
        "format_created_at",
    )
    list_filter = ("kind",)
