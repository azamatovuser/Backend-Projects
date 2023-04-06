from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def _login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("articles:list")
        return render(request, 'account/user404.html')
    return render(request, 'account/login.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect("articles:list")
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_path = request.GET.get('next')
            messages.success(request, "Muvaffaqiyatli login qildingiz")
            if next_path:
                return redirect(next_path)
            return redirect("articles:list")
    ctx = {
        'form': form
    }
    return render(request, 'account/login.html', ctx)


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('articles:list')
    if request.method == 'POST':
        logout(request)
        return redirect("account:login")
    return render(request, 'account/logout.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('articles:list')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'You was added successfully!')
        return redirect('account:login')
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)