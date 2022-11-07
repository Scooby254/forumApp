from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from .models import Question, Answer

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Successfully created for {username}! Login In Now')
            return redirect('login')
    else:
        form = CreateUserForm()

    return render(request, 'register.html', {'form': form})

def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                #IF A USER IS CREATING FOR THE FIRST TIME, HE/SHE SHOULD BE DIRECTED TO THE PROFILE SETTINGS PAGE, ELSE, HE/SHE SHOULD GO TO HIS/HER HOMEPAGE
                fname = user.profile.firstname
                if fname is None:
                    login(request, user)
                    return redirect('profile_settings')
                else:
                    login(request, user)
                    return redirect('home')
        else:
            messages.warning(request, 'Please enter the correct Username and Password. Note that both fields maybe case-sensitive.')
    form = AuthenticationForm()

    context={'login_form':form}
    return render(request, 'login.html', context)

@login_required
def logoutUser(request):
    logout(request)
    messages.warning(request, 'You have been logged out!')
    return redirect('login')

@login_required
def profile_settings(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid:
            form.save()
            messages.success(request, f'Account Successfully Updated!')
            return redirect('profile_settings')
        else:
            messages.warning(request, 'You have entered wrong details. Please give the correct details')
            return redirect('profile_settings')

    context = {'form':form}

    return render(request, 'profile_settings.html', context)

def home(request):
    return render(request, 'home.html')

#====================================================================================================================
#============================================ CRUD VIEWS HERE =======================================================

class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ['-created']

class QuestionDetailView(DetailView):
    model = Question


class QuestionCreateView(CreateView):
    model = Question
    fields = ['title', 'body']
    #exclude = ['user']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

