from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=25, blank=False, null=False)
    uom=models.CharField(max_length=10)
    price=models.FloatField()


