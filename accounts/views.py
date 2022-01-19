from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth.models import User

# Create your views here.
from .utils import DataMixin


class RegisterUser(DataMixin, SuccessMessageMixin, CreateView):
    """Show register form"""

    form_class = RegisterUserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy("login")
    error_message = "Registration error"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        c_def = self.get_user_context(
            title="Registration", ico="menu/img/ico/home_pink.png")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, SuccessMessageMixin, LoginView):
    """Autorization class"""

    form_class = LoginUserForm
    template_name = 'accounts/login.html'
    error_message = "Something went wrong"
    success_url = reverse_lazy("home")
    user = ""

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        c_def = self.get_user_context(
            title="Sign in", ico="menu/img/ico/home_pink.png")

        return dict(list(context.items()) + list(c_def.items()))


class LogoutUser(LoginRequiredMixin, LogoutView, SuccessMessageMixin):
    next_page = "home"
    success_message = "Logout successfully"
