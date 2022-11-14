from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Profile

def user_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='forum_users')
        instance.groups.add(group)

        Profile.objects.create(
            user=instance,
            email = instance.email,
            )
        print("Forum User Created!!!")
post_save.connect(user_profile, sender=User)
