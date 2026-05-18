from django.contrib import admin
from .models import Review
from common.admin import CommonAdmin


@admin.register(Review)
class ReivewAdmin(CommonAdmin):
    list_display = (
        "__str__",
        "payload",
        "format_created_at",
        "format_updated_at",
    )

    list_filter = ("rating",)
