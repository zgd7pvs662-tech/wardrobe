# users/urls.py
from django.urls import path
from .views import SignUpView

# Объявляем пространство имен для этого приложения
app_name = 'users'

urlpatterns = [
    # Имя маршрута 'signup', как мы и определили ранее
    path('signup/', SignUpView.as_view(), name='signup'),
]