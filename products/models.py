from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pt_sessions(models.Model):

    class Meta:
        verbose_name_plural = 'Pt_sessions'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null= True, blank= True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Subscriptions(models.Model):

    class Meta:
        verbose_name_plural = 'Subscriptions'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null= True, blank= True)
    description = models.TextField(max_length=100)
    include_1 = models.TextField(max_length=100, null= True, blank= True)
    include_2 = models.TextField(max_length=100, null= True, blank= True)
    include_3 = models.TextField(max_length=100, null= True, blank= True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name