from django.contrib import admin
from .models import Category
from common.admin import CommonAdmin


@admin.register(Category)
class CategoryAdmin(CommonAdmin):
    list_display = (
        "name",
        "kind",
    )
    list_filter = (
        "name",
        "kind",
    )
