from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    serie = models.CharField(max_length=250)
    price = models.IntegerField()

    class Meta:
        db_table = 'product'
