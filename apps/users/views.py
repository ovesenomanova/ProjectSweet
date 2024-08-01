from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from .forms import UserRegisterForm
from django.urls import reverse_lazy

class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy("users_login")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
