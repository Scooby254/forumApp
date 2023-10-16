from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from ckeditor.fields import RichTextField

departments = [('ICT', 'ICT'), ('ODG','ODG'),('Trees', 'Trees'), ('Soils', 'Soils'), ('Landscapes', 'Landscapes')]
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, blank=True)
    othernames = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    prof_pic = models.ImageField(default="user_pic.png", null=True, blank=True)
    department = models.CharField(max_length=50, choices=departments)
    last_seen = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.user.username.title()} - Profile'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.prof_pic.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.prof_pic.path)

class Tag(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag.title()
class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category.title()

class Question(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    body = RichTextField()
    #body = models.TextField(null=False, blank=False)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now = True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    likes = models.ManyToManyField(User, related_name='questions_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.title}  by {self.user.username} '

    def get_absolute_url(self):
        return reverse('questions_detail', kwargs={'pk':self.pk})

class Answer(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    content = RichTextField()
    responded_on = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, related_name="answer", on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return 'answer by {}'.format(self.user.username)
                #'%s - %s' %(self.question.title, self.content)#f'{self.user.username} - Answer'

    def children(self):
        return Answer.objects.filter(parent=self)

    def get_absolute_url(self):
        return reverse('questions_detail', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)