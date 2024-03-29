from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import Profile, Question, Answer

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'username': 'Username'}
        def save(self, commit=False):
            user = super(CreateUserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {"content":""}
        widgets = {
            'content':forms.TextInput(attrs={'class':'form-control'}),
            #'correct':forms.CheckboxInput()
        }
    
"""class ValidateAnswerForm(forms.ModelForm):
    #correct_flag = forms.BooleanField(required=False, label='Is this the Most Correct Answer?')
    class Meta:
        model = Answer
        fields = ['correct']
         widgets = {
            'correct':forms.CheckboxInput(attrs={'id':'correct', 'checked': ''}),
        }
        def __init__(self, *args, **kwargs):
            self.valcorrect = kwargs.pop("arg_correct")
            super(ValidateAnswerForm, self).__init__(*args, **kwargs)
            self.fields['correct'].initial = False
 """
