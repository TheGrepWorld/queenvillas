from django.db import models


# Create your models here.
# user_types=(('owner','OWNER'),('Broker','BROKER '),('Agent','AGENT'),('builder','BUILDER'))
class UserAccount(models.Model):
    full_name = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=12)
    email = models.CharField(max_length=100,unique=True)
    user_type=models.CharField(max_length=255, default='owner')

    def __str__(self):
        return self.email
