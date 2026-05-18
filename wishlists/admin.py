from django.contrib import admin
from common.admin import CommonAdmin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(CommonAdmin):
    list_display = (
        "name",
        "user",
        "format_created_at",
        "format_updated_at",
    )
