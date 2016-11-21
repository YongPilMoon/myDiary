from django.conf.urls import url

from member.views import ResetPasswordRequestView, PasswordResetConfirmView, LoginView, logout_view

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^reset_psw/$', ResetPasswordRequestView.as_view(), name='reset_psw'),
    url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        PasswordResetConfirmView.as_view(), name='reset_password_confirm'),
]
