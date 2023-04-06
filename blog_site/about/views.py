from django.shortcuts import render
from .models import Feedback


def about(request):
    feedbacks = Feedback.objects.all()
    ctx = {
        'feedback': feedbacks
    }
    return render(request, 'blogs/about.html', ctx)