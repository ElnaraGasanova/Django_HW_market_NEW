from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from users.models import User


class UserRegisterForm(UserCreationForm):
    '''Форма регистрации пользователя.'''
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class UserForgotPasswordForm(PasswordResetForm):
    pass
