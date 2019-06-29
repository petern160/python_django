from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=False, null=False)
    # null = true, default = true
    featured = models.BooleanField(default=False)
    # null has to deal with database can be empty or non empty
    # blank has to do with field
