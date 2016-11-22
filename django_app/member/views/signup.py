from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import login as auth_login
from member.forms import SignupModelForm

__all__ = [
    'SignupView',
]


class SignupView(FormView):
    template_name = 'member/login.html'
    form_class = SignupModelForm
    success_url = reverse_lazy('diary:month_calendar')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return super(SignupView, self).form_valid(form)


