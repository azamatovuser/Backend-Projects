from django.shortcuts import render, redirect, reverse
from .models import Article, Tag, Category_more
from django.shortcuts import get_object_or_404
from .form import EditForm, Createform
from django.contrib.auth.decorators import login_required


def list(request):
    articles = Article.objects.all()
    tags = Tag.objects.all()
    category = Category_more.objects.all()
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    q = request.GET.get('q')
    if q:
        articles = articles.filter(title__icontains=q)
    if tag:
        articles = articles.filter(tags__title=tag)
    if cat:
        articles = articles.filter(category__title=cat)
    ctx = {
        "object_list": articles,
        "category": category,
        "tags": tags,
    }
    return render(request, 'articles/list.html', ctx)


def detail(request, pk):
    user = request.user
    article = get_object_or_404(Article, id=pk)
    ctx = {
        'object': article,
    }
    return render(request, 'articles/detail.html', ctx)



@login_required
def edit(request, pk):
    user = request.user
    article = get_object_or_404(Article, id=pk)
    if article.author != user:
        if not user.is_superuser:
            return render(request, 'articles/notyou.html',)
    form = EditForm(instance=article)
    if request.method == 'POST':
        form = EditForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("articles:list")
    ctx = {
        'form': form
    }
    return render(request, 'articles/edit.html', ctx)


@login_required
def delete(request, pk):
    article = get_object_or_404(Article, id=pk)
    if article.author != user:
        if not user.is_superuser:
            return render(request, 'articles/notyou.html',)
    if request.method == 'POST':
        article.delete()
        return redirect("articles:list")
    ctx = {
        "object": article
    }
    return render(request, 'articles/delete.html', ctx)


@login_required
def create(request):
    form = Createform()
    if request.method == 'POST':
        form = Createform(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('articles:list')
    ctx = {
        'form': form
    }
    return render(request, 'articles/create.html', ctx)
