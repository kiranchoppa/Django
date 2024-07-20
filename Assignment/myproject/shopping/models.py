from django.db import models


# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default="default.png", blank=True)
    price = models.IntegerField()
    discount = models.FloatField()
    sizes = {
        "xs": "extra small",
        "s": "small",
        "m": "medium",
        "l": "large",
        "xl": "extra large",
    }
    size = models.CharField(choices=sizes, max_length=2, default="m")
    discription = models.TextField(null=True, blank=True)
