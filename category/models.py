from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=15, blank=False, null=False)
    parent = models.ForeignKey('self',  null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User)
