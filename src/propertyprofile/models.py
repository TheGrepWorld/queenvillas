from django.db import models

# Create your models here.
class PropertyProfile(models.Model):
    area=models.CharField(max_length=255)
    dimension=models.CharField(max_length=299)
    floors=models.CharField(max_length=340)