from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'accounts/login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'accounts/register.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
