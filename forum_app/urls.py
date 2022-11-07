from django.urls import path
from . import views

urlpatterns = [
    #=================USER PROFILES URLS=====================
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile_settings, name='profile_settings'),

    #=====================CRUD URLS===========================
    path('questions/', views.QuestionListView.as_view(), name='questions_list'),
    path('questions/new/', views.QuestionCreateView.as_view(), name='questions_create'),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name='questions_detail'),

]