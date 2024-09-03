from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth import logout
from authentication.models import CustomUser
from authentication.forms import CustomUserCreationForm
from .forms import LoginForm

@login_required(login_url='/register/')
def home(request):
    first_name = request.session.get('first_name', 'Guest')
    role_id = request.session.get('role', 0)
    role_name = dict(CustomUser.ROLE_CHOICES).get(role_id, 'Unknown')
    print(f"Home View Data: first_name={first_name}, role={role_name}")
    context = {
        'first_name': first_name,
        'role': role_name
    }

    return render(request, template_name='index.html', context=context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, request=request)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Logged in successfully!')
                request.session['first_name'] = user.first_name
                request.session['role'] = user.role
                return redirect('home')
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

