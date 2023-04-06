from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You did log in!')
            return redirect("blogs:index")
    ctx = {
        "form": form
    }
    return render(request, 'account/login.html', ctx)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.warning(request, 'You did logout')
        return redirect("blogs:index")
    return render(request, 'account/logout.html')


def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("account:login")
    ctx = {
        "form": form
    }
    return render(request, 'account/register.html', ctx)