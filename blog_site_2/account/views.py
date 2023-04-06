from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from blogs.models import Article


def login_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_path = request.GET.get('next')
            messages.success(request, 'Login boldi!!!')
            if next_path:
                return redirect(next_path)
            return redirect("blogs:index")
    ctx = {
        "form": form
    }
    return render(request, 'account/login.html', ctx)


def logout_view(request):
    if request.method == "POST":
        logout(request)
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