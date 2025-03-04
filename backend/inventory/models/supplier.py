from django.db import models

class Supplier(models.Model):
    id = models.CharField(max_length=255, null = False, primary_key=True)
    name = models.CharField(max_length=255,null=True)
    phoneNumber = models.CharField(max_length=255, null=True)
    region = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name