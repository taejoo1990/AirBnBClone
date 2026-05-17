from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoice(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        JP = ("jp", "Japanese")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        KRW = "krw", "KRW"
        USD = "usd", "USD"
        JPN = "jpn", "JPN"

    avatar = models.ImageField(blank=True)
    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    name = models.CharField(
        max_length=150,
        default="",
    )
    is_host = models.BooleanField(
        verbose_name="ホスト",
        default=False,
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoice.choices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        max_length=3,
        choices=CurrencyChoices.choices,
    )
