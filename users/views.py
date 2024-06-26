import random
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, TemplateView
from users.forms import UserRegisterForm
from users.forms import UserForgotPasswordForm
from users.models import User
import secrets
from django.conf import settings
from django.core.mail import send_mail


class UserRegisterView(CreateView):
    '''Класс регистрации нового пользователя.'''
    model = User
    form_class = UserRegisterForm

    def get_success_url(self):
        return reverse('users:login')

    def form_valid(self, form):
        #при рег-ции добавляем польз-лю токен
        token = secrets.token_hex(8)
        user = form.save()
        user.token = token
        #после рег-ции польз-ль не м.зайти,т.к.не подтвердил почту,значит еще не активен!
        user.is_active = False
        user.save()
        host = self.request.get_host()
        link = f'http://{host}/users/confirm_register/{token}/'
        message = f'Вы зарегистрировались на сайте Маркета "ВкусВилл". Подтвердите почту {link})'
        send_mail('Верификация почты', message, settings.EMAIL_HOST_USER,
                  ['skypro.msk@yandex.ru'])
        return super().form_valid(form)


def confirm_email(request, token):
    #если юзер не найден, то:
    user = get_object_or_404(User, token=token)
    #после того, как польз-ль подтвердил почту - он м.войти в сис-му:
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class UserForgotPasswordView(PasswordResetView):
    '''Класс восстановления пароля.'''
    form_class = UserForgotPasswordForm
    template_name = 'users/reset_password.html'
    email_template_name = 'users/new_password.html'

    def get_success_url(self):
        return reverse('users:new_password')


    def form_valid(self, form):
        '''Получение данных из формы и отправка сообщений о смене пароля.'''
        email = form.cleaned_data.get('email')
        user = User.objects.get(email=email)
        new_password = ''.join([str(random.randint(0, 9)) for num in range(8)])
        user.set_password(new_password)
        user.save()
        send_mail('Смена пароля', f'Ваш новый пароль {new_password}', settings.EMAIL_HOST_USER,
                  [user.email])
        return super().form_valid(form)


class NewPasswordView(TemplateView):
    template_name = 'users/new_password.html'
