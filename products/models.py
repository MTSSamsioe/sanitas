from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categories(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null= True, blank= True)
    
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Products(models.Model):

    class Meta:
        verbose_name_plural = 'Products'

    category = models.ForeignKey('Categories', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null= True, blank= True)
    description = models.TextField(max_length=500)
    include_1 = models.TextField(max_length=254, null= True, blank= True)
    include_2 = models.TextField(max_length=254, null= True, blank= True)
    include_3 = models.TextField(max_length=254, null= True, blank= True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Appointments(models.Model):

    class Meta:
        verbose_name_plural = 'Appointments'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_time = models.DateTimeField(null=True, blank=False)
    
    

    def __str__(self):
        return 'Appointments'