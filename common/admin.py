from django.contrib import admin


class CommonAdmin(admin.ModelAdmin):

    def format_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d")

    format_created_at.short_description = "作成時間"

    def format_updated_at(self, obj):
        return obj.updated_at.strftime("%Y-%m-%d")

    format_updated_at.short_description = "修正時間"
    readonly_fields = (
        "format_created_at",
        "format_updated_at",
    )
