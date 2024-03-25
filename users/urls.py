from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from users.apps import UsersConfig
from users.views import UserRegisterView, confirm_email

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', UserRegisterView.as_view(), name='registration'),
    path('confirm_register/<str:token>/', confirm_email, name='confirm_email'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#temlate_name='users/login.html'
