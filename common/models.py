from django.db import models


class CommonModel(models.Model):
    """Common Model Definition"""

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="作成時間",
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="修正時間",
    )

    class Meta:
        abstract = True
