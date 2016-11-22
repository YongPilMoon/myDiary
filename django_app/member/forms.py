from django import forms
from django.contrib.auth import password_validation

from member.models import DiaryUser


class SignupModelForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput()
    )

    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput()
    )

    class Meta:
        model = DiaryUser
        fields = (
            'email',
            'nickname',
            'password1',
            'password2',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        password_validation.validate_password(
            self.cleaned_data['password1'],
            self.instance
        )

    def save(self, commit=True):
        user = super(SignupModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.save()
        return user


class PasswordResetRequestForm(forms.Form):
    email = forms.CharField(label=('Email'), max_length=254)


class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
        }
    new_password1 = forms.CharField(label=("New password"),
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=("New password confirmation"),
                                    widget=forms.PasswordInput)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                    )
        return password2


class LoginForm(forms.Form):
    email = forms.CharField(
        label=(),
        max_length=254,
        widget=forms.EmailInput(
            attrs={'class': 'login-input', 'placeholder': '이메일'}
        ))

    password = forms.CharField(
        label=(),
        widget=forms.PasswordInput(
            attrs={'class': 'login-input', 'placeholder': '비밀번호'}
        ))
