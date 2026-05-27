from django.db import models
from common.models import CommonModel


class Experience(CommonModel):
    """Experience Model Definition"""

    name = models.CharField(
        max_length=250,
    )
    descrption = models.TextField()
    country = models.CharField(
        max_length=50,
        default="JAPAN",
    )
    city = models.CharField(
        max_length=80,
        default="Tokyo",
    )
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="experience",
    )
    price = models.PositiveIntegerField()
    address = models.CharField(
        max_length=250,
    )
    start = models.TimeField()
    end = models.TimeField()
    perks = models.ManyToManyField(
        "experiences.Perks",
        related_name="experience",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="experience",
    )

    def __str__(self) -> str:
        return self.name


class Perks(CommonModel):
    """What is included on an Experiences"""

    name = models.CharField(
        max_length=100,
    )
    details = models.CharField(
        max_length=250,
    )
    explanation = models.TextField()

    class Meta:
        verbose_name_plural = "Perks"

    def __str__(self) -> str:
        return self.name
