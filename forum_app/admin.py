from profile import Profile
from django.contrib import admin
from .models import Profile, Tag, Category, Question, Answer

admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)