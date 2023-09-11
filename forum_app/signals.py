from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from . models import Answer
from .models import Profile

#SIGNAL TO ADD A NEW USER TO A CERTAIN GROUP
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

#SIGNAL FOR NOTIFICATION CREATION WHEN A NEW COMMENT/ANSWER IS POSTED FOR A QUESTION
def user_comment_post(sender, instance, created, **kwargs):
    if created:
        comment = instance
        post = comment.question
        #reply = comment.reply
        #text_preview = comment.text[:90]
        sender = comment.user
        #notify = Notification.objects.create(post=post, sender=sender, comment=comment, user=post.author, text_preview=text_preview, notification_type=2)
        #notify.save()
        print(f"{sender} replied to your question")
post_save.connect(user_comment_post, sender=Answer)