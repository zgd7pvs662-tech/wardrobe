# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # Указываем поля для отображения в списке
    list_display = ('email', 'username', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active', 'groups',)
    
    # Явно определяем поля для редактирования, чтобы избежать дублирования
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Поля для создания пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password', 'password2'),
        }),
    )
    
    search_fields = ('email', 'username',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)