# users/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    # После успешной регистрации перенаправляем на страницу входа
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'