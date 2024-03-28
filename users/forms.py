from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from users.models import User


class UserRegisterForm(UserCreationForm):
    '''Форма регистрации пользователя.'''
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class UserForgotPasswordForm(PasswordResetForm):
    '''Форма восстановления пароля пользователя.'''

    class Meta:
        model = User
        fields = ['email',]

    def clean_email(self):
        '''Проверка существующего пользователя.'''
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
        except Exception:
            raise forms.ValidationsError('Пользователь с такой почтой не найден.')
        return email

    def send_mail(
            self,
            subject_template_name,
            email_template_name,
            context,
            from_email,
            to_email,
            html_email_template_name=None,
    ):
        pass

    # def get_success_url(self):
    #     return reverse('users:login')
    # success_message = 'Письмо восстановления пароля направлено на email.'


# class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
#     '''Класс подтверждения восстановления пароля.'''
#     form_class = UserPasswordResetConfirmForm
#
#     def get_success_url(self):
#         return reverse('users:login')
#     success_message = 'Пароль восстановлен.'
