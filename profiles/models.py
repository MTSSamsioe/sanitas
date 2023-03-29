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


'''
Code below is taken from boutique ado walk through project
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/
250e2c2b8e43cccb56b4721cd8a8bd4de6686546/profiles/models.py
'''


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Creates or updates a users profile
    """

    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
