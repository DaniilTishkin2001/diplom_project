from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect,reverse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView

from .forms import AuthUserForm, RegisterUserForm


class MyprojectLoginView(LoginView):
    template_name = "users/login.html"
    form_class = AuthUserForm
    success_url = reverse_lazy("home")
    def get_success_url(self):
        return self.success_url

class RegisterUserView(CreateView):
    model = User
    template_name = "users/register_page.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("home")
    success_msg = "Пользователь успешно создан"

    def form_valid(self,form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        auth_user = authenticate(username = username,password=password)
        login(self.request,auth_user)
        return form_valid


class MyProjectLogout(LogoutView):
    next_page = reverse_lazy("home")


