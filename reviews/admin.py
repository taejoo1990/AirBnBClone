from django.contrib import admin
from .models import Review
from common.admin import CommonAdmin


class BadRatingFilter(admin.SimpleListFilter):
    title = "Filter Bad review"
    parameter_name = "water"

    def lookups(self, request, model_admin):
        return [
            ("up", "2👆"),
            ("down", "2👇"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word == "up":
            return reviews.filter(rating__gte=2)
        elif word == "down":
            return reviews.filter(rating__lt=2)
        else:
            return reviews


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "tomato"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        print(word)
        return reviews if word == None else reviews.filter(payload__contains=word)


@admin.register(Review)
class ReivewAdmin(CommonAdmin):
    list_display = (
        "__str__",
        "payload",
        "format_created_at",
        "format_updated_at",
    )

    list_filter = (
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
        WordFilter,
        BadRatingFilter,
    )
