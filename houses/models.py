from django.db import models

""" Model definition for Houses """
class House(models.Model):
    name = models.CharField(verbose_name="件名",max_length=140)
    price_per_day = models.PositiveIntegerField(verbose_name="料金")
    discription = models.TextField(verbose_name="紹介")
    address = models.CharField(max_length=200)
    pets_allowd = models.BooleanField(verbose_name="ペット可",default=True,help_text="Does this house allow pets?")

    def __str__(self):
        return self.name;
    