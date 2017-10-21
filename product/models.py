from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=25, blank=False, null=False)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    uom=models.CharField(max_length=10)
    price=models.FloatField()

    def __str__(self):
        return self.name


