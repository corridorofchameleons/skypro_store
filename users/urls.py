from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, EmailSentView, PasswordChanged, \
    PasswordReset

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email_sent/', EmailSentView.as_view(), name='email_sent'),
    path('verification/<str:token>/', email_verification, name='verified'),
    path('reset_password/', PasswordReset.as_view(), name='reset_password'),
    path('password_changed/', PasswordChanged.as_view(), name='password_changed'),
]
