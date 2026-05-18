from django.contrib import admin
from .models import Experience, Perks
from common.admin import CommonAdmin


@admin.register(Experience)
class ExperiencesAdmin(CommonAdmin):
    list_display = (
        "name",
        "price",
        "start",
        "end",
        "format_created_at",
        "format_updated_at",
    )
    list_filter = ("category",)


@admin.register(Perks)
class PerksAdmin(CommonAdmin):
    list_display = (
        "name",
        "explanation",
        "format_created_at",
        "format_updated_at",
    )
