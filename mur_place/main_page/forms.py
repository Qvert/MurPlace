from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username', min_length=5, max_length=50)
    email = forms.EmailField(max_length=254,
                             help_text='Обязательное поле. Введите '
                                       'действующий email.')
    first_name = forms.CharField(label='First Name',
                                 min_length=3,
                                 max_length=50)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
