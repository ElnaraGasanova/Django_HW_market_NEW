from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''Отображение пользователей в Админке'''
    list_display = ('email', 'phone',)
    list_filter = ('country',)
    search_fields = ('email', 'phone',)