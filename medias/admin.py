from django.contrib import admin
from common.admin import CommonAdmin
from .models import Photo, Video


@admin.register(Photo)
class PhotoAdmin(CommonAdmin):
    pass


@admin.register(Video)
class VedioAdmin(CommonAdmin):
    pass
