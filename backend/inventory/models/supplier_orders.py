from django.db import models

class SupplierOrders(models.Model):
    id = models.CharField(max_length=255, null = False, primary_key=True)
    supplierId = models.CharField(max_length=255,null=False)
    productId = models.CharField(max_length=255, null=False)
    productAmount = models.IntegerField()
    deliveryStatus = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name