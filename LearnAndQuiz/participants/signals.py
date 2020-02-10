from django.db.models.signals import post_save #fired when user(object) is saved 
from django.contrib.auth.models import User #signal sender
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)#when an user is created, sends post_save signal which will be recieved by receiver func
def create_profile(sender, instance, created, **kwargs):
	if created: #if an user is created,creates a profile object
		Profile.objects.create(participants=instance)#creates a profile of the current user instance.

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs): #kwargs accepts additional keyword arguments
	instance.profile.save() #saves the profile