# users/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # Указываем поля для формы СОЗДАНИЯ
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # Указываем поля для формы РЕДАКТИРОВАНИЯ
        fields = ('username', 'email', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')