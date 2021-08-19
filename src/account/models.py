from django.db import models


# Create your models here.
class UserAccount(models.Model):
    full_name = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=12)
    email = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.email
