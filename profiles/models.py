from django.db import models

class Profile(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.email
