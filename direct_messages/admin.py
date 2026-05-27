from django.contrib import admin
from common.admin import CommonAdmin
from .models import ChatRoom, Message


@admin.register(ChatRoom)
class RoomAdmin(CommonAdmin):
    list_display = (
        "__str__",
        "format_created_at",
        "format_updated_at",
    )


@admin.register(Message)
class MessageAdmin(CommonAdmin):
    list_display = (
        "__str__",
        "format_created_at",
        "format_updated_at",
    )
