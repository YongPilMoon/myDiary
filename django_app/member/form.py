from django import forms


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
