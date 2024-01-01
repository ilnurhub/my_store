import random

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:email_verify')
    template_name = 'users/register.html'

    def form_valid(self, form):
        self.object = form.save()
        self.object.secret_key = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        self.object.save()
        send_mail(
            subject='Верификация электронной почты',
            message=f'Секретный код для верификации электронной почты: {self.object.secret_key}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)


def email_verification(request):
    context = {
        'card_title': 'На Ваш email выслан секретный ключ. Введите его в поле для верификации Вашей почты.'
    }
    users = User.objects.all()
    if request.method == 'POST':
        secret_key = request.POST.get('secret_key')
        for user in users:
            if user.secret_key == secret_key:
                user.is_active = True
                user.save()
                return HttpResponseRedirect(reverse('users:login'))
            else:
                context = {
                    'card_title': 'Неверный ключ. Попробуйте ещё раз'
                }
    return render(request, 'users/email_verification.html', context=context)


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user
