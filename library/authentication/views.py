from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.shortcuts import render, get_object_or_404
from .forms import CustomUserCreationForm


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

# def register(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         middle_name = request.POST.get('middle_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         role = request.POST.get('role')
#
#         role = int(role) if role.isdigit() else 0
#
#         # Validate and create user
#         if len(first_name) <= 20 and len(last_name) <= 20 and len(email) <= 100:
#             if CustomUser.objects.filter(email=email).exists():
#                 messages.error(request, 'Email is already in use.')
#             else:
#                 is_staff=True if role ==1 else False
#                 is_superuser = True if role == 1 else False
#                 custom_user = CustomUser.objects.create_user(
#                     email=email,
#                     password=password,
#                     first_name=first_name,
#                     middle_name=middle_name,
#                     last_name=last_name,
#                     role=role,
#                     is_active=True,
#                     is_staff=is_staff,
#                     is_superuser=is_superuser
#                 )
#                 custom_user.save()
#                 messages.success(request, 'User registered successfully!')
#                 user = authenticate(request, email=email, password=password)
#                 if user is not None:
#                     login(request, user)
#                     request.session['first_name'] = first_name
#                     request.session['role'] = role
#                     return redirect('home')
#         else:
#             messages.error(request, 'Invalid input data.')


@login_required(login_url='/login/')
def users(request):

    all_users = CustomUser.objects.all()
    context = {
        'users': all_users
    }
    return render(request, 'users.html', context)