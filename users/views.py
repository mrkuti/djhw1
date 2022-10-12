from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.urls import reverse
from django.views import generic
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .forms import RegistrationForm, LoginForm, MyPasswordChangeForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.urls import reverse_lazy








#
#
# class Login(LoginView):
#     form_class = LoginView
#     template_name = "login.html"
#     success_url = "/all_brands/"
#
#     def get_success_url(self):
#         return self.success_url
#


# # @login_required
# def profile(request):
#     return render(request, 'profile.html')





class RegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = "register.html"
    success_url = "/login/"


# class NewLoginView(LoginView):
#     form_class = LoginForm
#     template_name = "registration/account.html"
#     success_url = "/all_brands/"

    # def get_success_url(self):
    #     return self.success_url

def profile(request):
    return render(request, 'profile.html')

class MyPasswordChangeView(PasswordChangeView):
    template_name = "registration/account.html"
    success_url = reverse_lazy("users:change")


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "registration/account_change.html"
