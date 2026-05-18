from django.db import models
from common.models import CommonModel


class Wishlist(CommonModel):
    """Wishlist Model Definition"""

    name = models.CharField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ManyToManyField(
        "rooms.Room",
        blank=True,
    )
    experiences = models.ManyToManyField(
        "experiences.Experience",
        blank=True,
    )
