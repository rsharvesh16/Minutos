#
#

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist



#
# Models

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    active_team_id = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='uploads/avatars/', blank=True, null=True)

    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return '/static/images/avatar.png'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.userprofile.save()
    except ObjectDoesNotExist:
        Userprofile.objects.create(user=instance)