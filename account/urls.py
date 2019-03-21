from django.urls import path
from django.views.generic import RedirectView
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login',user_login,name='login'),
    path('logout',user_logout,name='logout'),
    path('register',register,name='register'),
    path('password-change',auth_views.PasswordChangeView,name='password_change'),
    path('password-change-done',auth_views.PasswordChangeDoneView,name='password_change_done'),
]