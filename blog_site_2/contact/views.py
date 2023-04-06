from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from blogs.models import Article, Category, Tag, Comment


def contact(request):
    articles = Article.objects.all()
    last_art = Article.objects.all()[:3]
    tags = Tag.objects.all()
    categories = Category.objects.all()
    cat = request.GET.get('cat')
    q = request.GET.get('q')
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if q:
        articles = articles.filter(title__icontains=q)
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact:index')
    ctx = {
        'form': form,
        "object_list": articles,
        "tags": tags,
        "last_art": last_art,
        "categories": categories,
    }
    return render(request, 'blogs/contact.html', ctx)