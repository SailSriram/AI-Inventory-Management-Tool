from django.db import models

class Product(models.Model):
    id = models.CharField(max_length=255, primary_key=True,null=False)
    productName = models.CharField(max_length=255)
    productDescription = models.TextField(blank=True, null=True)
    productType = models.CharField(max_length=255)
    productQuantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name