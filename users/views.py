from django.contrib.auth.views import LoginView as BaseLoginView
from django.shortcuts import render


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
