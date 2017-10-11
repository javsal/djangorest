# Create your models here.
# api/models.py

from django.db import models

GENDER_CHOICES = (
    ('M','Male'),
    ('F', 'Female')
)

PLAYER_TYPE=(
    ('BATING', 'Bating'),
    ('BOWLER', 'Bowler'),
    ('ALLROUNDER', 'All Rounder'),
    ('KEEPER', 'Keeper')
)

class DistrictList(models.Model):
    name=models.CharField(max_length=15, blank=False, unique=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class PlayerList(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='F')
    palyer_type= models.CharField(max_length=10, choices=PLAYER_TYPE, default='BOWLER')
    home_district=models.ForeignKey(DistrictList, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)