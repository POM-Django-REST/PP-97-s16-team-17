from django import forms
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Enter your password.",
    )
    password2 = forms.CharField(
        label="Confirm Password please",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'role')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['email'].widget = forms.EmailInput(
            attrs={'placeholder': 'Enter your email', 'class': 'form-control'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['middle_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['role'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['role'].choices = CustomUser.ROLE_CHOICES

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('A user with this email already exists.')
        if len(email) > 100:
            raise forms.ValidationError("Email must be 100 characters or fewer.")
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) > 20:
            raise forms.ValidationError("First name must be 20 characters or fewer.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) > 20:
            raise forms.ValidationError("Last name must be 20 characters or fewer.")
        return last_name

    def clean_role(self):
        # Ensure role is an integer and set default if not
        role = self.cleaned_data.get('role', 0)
        if not isinstance(role, int):
            raise forms.ValidationError("Invalid role selected.")
        return role

    def save(self, commit=True):
        # Save the provided password in hashed format and set user attributes
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        role = self.cleaned_data.get('role')

        user.is_staff = True if role == 1 else False
        user.is_superuser = True if role == 1 else False
        user.is_active = True  # You set `is_active` to True when creating the user

        if commit:
            user.save()
        return user