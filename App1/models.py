from django.db import models

# Create your models here.
class BikeData(models.Model):
    bike_company = models.CharField(max_length=150)
    bike_name = models.CharField(max_length=150)
    bike_fueltype = models.CharField(max_length=150)
    bike_modelyear = models.CharField(max_length=150)
    
