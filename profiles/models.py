from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    """ Models that stores user information """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    preset_full_name = models.CharField(max_length=100, null=True, blank=True)
    preset_email = models.EmailField(max_length=254, null=True, blank=True)
    preset_adress = models.CharField(max_length=100, null=True, blank=True)
    preset_post_code = models.CharField(max_length=20, null=True, blank=True)
    preset_city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username

# Most of the structure, logic are taken from Code institute project lessons Boutique ado
@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Creates or updates a users profile
    """

    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()