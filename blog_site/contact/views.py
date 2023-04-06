from django.shortcuts import render, reverse, redirect
from .models import Contact
from .forms import ContactForms
from django.contrib import messages


def contact(request):
    form = ContactForms(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your message successfully sent!')
        return redirect('contact:index')
    ctx = {
        'form': form
    }
    return render(request, 'blogs/contact.html', ctx)

