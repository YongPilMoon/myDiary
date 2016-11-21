from django.contrib.auth import authenticate as auth_authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from member.form import LoginForm

__all__ = [
    'LoginView',
]


class LoginView(FormView):
    template_name = 'member/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('diary:month_calendar')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user = auth_authenticate(email=email, password=password)

        if user is not None:
            auth_login(self.request, user)
        else:
            return HttpResponse('아이디와 비밀번호를 확인해주세요')

        return super().form_valid(form)
