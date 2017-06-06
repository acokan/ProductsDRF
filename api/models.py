from __future__ import unicode_literals

from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    color = models.CharField(max_length=50)
    product_type = models.ForeignKey(ProductType)

    def __unicode__(self):
        return self.name
