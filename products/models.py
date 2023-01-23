from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pt_sessions(models.Model):

    class Meta:
        verbose_name_plural = 'Pt_sessions'

    user = models.ForeignKey(User,null=True ,on_delete=models.SET_NULL)
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

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null= True, blank= True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name