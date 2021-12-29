from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='RegisterView'),
    path('profile/', views.ProfilePageView.as_view(), name='ProfilePageView'),
    path('profile-edit/', views.ProfileEditView.as_view(), name='ProfileEditView'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]