from profile import Profile
from django.contrib import admin
from .models import Profile, Tags, Categories, Question, Answer

admin.site.register(Profile)
admin.site.register(Tags)
admin.site.register(Categories)
admin.site.register(Question)
admin.site.register(Answer)