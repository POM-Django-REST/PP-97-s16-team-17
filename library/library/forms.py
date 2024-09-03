from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.core.validators import validate_email

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        max_length=100
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
    )
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            # Authenticate the user
            user = authenticate(request=self.request, email=email, password=password)

            if user is None:
                self.add_error(None, "Invalid email or password.")

        return cleaned_data