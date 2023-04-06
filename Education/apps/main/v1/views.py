from django.shortcuts import render, redirect, reverse
from .forms import ContactForm, SubscribeForm
from apps.main.models import FAQ, Answer, Category
from ...course.models import Course
from ...blog.models import Post
from ...account.models import Profile


def index(request):
    categories = Category.objects.all()
    search = request.GET.get('search')
    courses = Course.objects.all()[:6]
    teachers = Profile.objects.filter(role=1).order_by('?')[:3]
    post = Post.objects.first()
    four_posts = Post.objects.all().exclude(id=post.id)[:4]
    forms = SubscribeForm()
    if request.method == "POST":
        forms = SubscribeForm(data=request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('.')
    ctx = {
        'courses': courses,
        'categories': categories,
        'post': post,
        'four_posts': four_posts,
        'forms': forms,
        'teachers': teachers
    }
    return render(request, 'main/index.html', ctx)


def about(request):
    questions = FAQ.objects.all()
    forms = SubscribeForm()
    if request.method == "POST":
        forms = SubscribeForm(data=request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('.')
    ctx = {
        'forms': forms,
        'questions': questions
    }
    return render(request, 'main/about.html', ctx)


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('.')
    forms = SubscribeForm()
    if request.method == "POST":
        forms = SubscribeForm(data=request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('.')
    ctx = {
        'form': form,
        'forms': forms,
    }
    return render(request, 'main/contact.html', ctx)