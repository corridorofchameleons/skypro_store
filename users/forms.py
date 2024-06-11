from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'country']


class PasswordResetForm(forms.Form):
    email = forms.EmailField(max_length=40, label='Введите почту, указанную при регистрации')
