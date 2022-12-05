from django.urls import path
from . import views

urlpatterns = [
    #=================USER PROFILES URLS=====================
    path('', views.QuestionListView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile_settings, name='profile_settings'),

    #=====================CRUD URLS===========================
    path('questions/', views.QuestionListView.as_view(), name='questions_list'),
    path('questions/new/', views.QuestionCreateView.as_view(), name='questions_create'),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name='questions_detail'),
    path('questions/<int:pk>/update', views.QuestionUpdateView.as_view(), name='questions_update'),
    path('questions/<int:pk>/delete', views.QuestionDeleteView.as_view(), name='questions_delete'),
    path('questions/<int:pk>/answer', views.AddAnswerView.as_view(), name='questions_answer'),
    path('like/<int:pk>', views.like_view, name='like_post'),

]