from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=25, blank=False, null=False)
    is_featured=models.BooleanField(default=False)
    parent=models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=25, blank=False, null=False)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    uom=models.CharField(max_length=10)
    price=models.FloatField()

    def __str__(self):
        return '%s %s %s %s' % (self.name, self.category.name, self.price, self.uom)


