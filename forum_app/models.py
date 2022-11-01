from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

departments = [('ICT', 'ICT'), ('ODG','ODG'),('Trees', 'Trees'), ('Soils', 'Soils'), ('Landscapes', 'Landscapes')]
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    prof_pic = models.ImageField(default="", null=True, blank=True)
    department = models.CharField(max_length=50, choices=departments)
    last_seen = models.DateTimeField()

class Tags(models.Model):
    tag = models.CharField(max_length=20)

class Categories(models.Model):
    category = models.CharField(max_length=50)

class Question(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now = True)
    categories = models.ManyToManyField(Categories)
    tags = models.ManyToManyField(Tags)
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='questions_post')
    
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.user.username} - Question'

class Answer(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    answer = models.TextField()
    responded_on = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)






