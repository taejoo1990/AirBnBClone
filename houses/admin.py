from django.contrib import admin
from .models import House

# Register your models here.
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    fields = ("name","discription","price_per_day","address","pets_allowd",)

    list_display = (
        "name",
        "price_per_day",
        "pets_allowd",
        "address",
    )
    
    list_filter = (
        "name",
        "price_per_day",
    )
    list_display_links = ("name","address")
    
    search_fields = "address",

    list_editable = "pets_allowd",

    