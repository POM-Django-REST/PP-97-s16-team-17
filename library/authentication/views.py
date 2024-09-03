from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import CustomUserCreationForm
from rest_framework import viewsets
from .serializers import CustomUserSerializer


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User registered successfully!')

            # Authenticate and log in the user
            user = authenticate(request, email=user.email, password=form.cleaned_data.get('password1'))
            if user is not None:
                login(request, user)
                request.session['first_name'] = user.first_name
                request.session['role'] = user.role
                return redirect('home')
        else:
            messages.error(request, 'Invalid input data.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


@login_required(login_url='/login/')
def users(request):

    all_users = CustomUser.objects.all()
    context = {
        'users': all_users
    }
    return render(request, 'users.html', context)

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer