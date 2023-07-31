from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUserForm, ProfileForm, AnswerForm, ValidateAnswerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Question, Answer
from django.urls import reverse, reverse_lazy

#REGISTER A NEW USER
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

#LOGIN FUNCTION
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

#LOGOUT A LOGGED IN USER
@login_required
def logoutUser(request):
    logout(request)
    messages.warning(request, 'You have been logged out!')
    return redirect('login')

#USER PROFILE TO ADD DETAILS SUCH AS PROFILE IMAGE AND DEPARTMENT
#WILL USE "Profile" MODEL CLASS WHICH UTILIZES 'PILLOW' LIBRARY FOR IMAGES PROCESSING
@login_required
def profile_settings(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid:
            form.save()
            messages.success(request, 'Account Successfully Updated!')
            return redirect('profile_settings')
        else:
            messages.warning(request, 'You have entered wrong details. Please give the correct details')
            return redirect('profile_settings')

    context = {'form':form}

    return render(request, 'profile_settings.html', context)


#HOMEPAGE SHOWING LIST OF ALL RECENT ASKED QUESTIONS
def home(request):

    return render(request, 'forum_app/question_list.html')

#========================================================================================================================
#============================================ CRUD CBV VIEWS HERE =======================================================
#========================================================================================================================

#LIKES FUNCTION TO CHECK IF A USER HAS LIKED A QUESTION, IF LIKED, IT INCREMENTS THE LIKES COUNT
def like_view(request, pk):
    post = get_object_or_404(Question, id=request.POST.get('question_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('questions_detail', args=[str(pk)]))

#CBV FOR LISTING QUESTIONS FROM THE "Question" MODEL CLASS/TABLE
class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ['-created']

#CBV FOR DISPLAY OF DETAILS OF AN INDIVIDUAL QUESTION
class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, *args, **kwargs):
        context = super(QuestionDetailView, self).get_context_data()
        a = get_object_or_404(Question, id=self.kwargs['pk'])
        total_likes = a.total_likes()
        liked = False

        if a.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

#CBV FOR CREATING A NEW QUESTION/DISCUSSION
class QuestionCreateView(CreateView, LoginRequiredMixin):
    model = Question
    fields = ['title', 'body', 'tags']
    #exclude = ['user']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#CBV FOR UPDATING/EDITING A QUESTION/DISCUSSION BY THE USER WHO POSTED THE QUESTION
class QuestionUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        else:
            return False

#DELETE VIEW FOR A QUESTION/DISCUSSION, ONLY THE USER WHO POSTED THE QUESTION CAN DELETE IT
class QuestionDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Question
    success_url = "/"
    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        else:
            return False

#CREATE VIEW FOR A RESPONSE TO A PARTICULAR DISCUSSION/QUESTION
class AddAnswerView(CreateView, LoginRequiredMixin):
    form_class = AnswerForm
    template_name = "forum_app/question_answer.html"

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url= reverse_lazy('questions_list')
''' 
class AnswerDetailView(CreateView, LoginRequiredMixin):
    model = Answer
    form_class = AnswerForm
    template_name = "forum_app/question_detail.html"

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url= reverse_lazy('questions_detail') '''

#VALIDATE ANSWER VIEW
class ValidateAnswerView(UpdateView, LoginRequiredMixin):
    model = Answer
    form_class = ValidateAnswerForm
    template_name = "forum_app/validate_answer.html"


