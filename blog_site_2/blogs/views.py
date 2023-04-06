from django.shortcuts import render, reverse, redirect, get_object_or_404, get_list_or_404, HttpResponse
from .models import Article, Comment, Category, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm


def footer(request):
    last_art = Article.objects.all()[:3]
    ctx = {
        "last_art": last_art
    }
    return render(request, 'footer.html', ctx)


def index(request):
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
    page_num = request.GET.get('page')
    paginator = Paginator(articles, 1)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    ctx = {
        "object_list": page_obj,
        "tags": tags,
        "last_art": last_art,
        "categories": categories,
    }
    return render(request, 'blogs/index.html', ctx)


def list(request):
    articles = Article.objects.all()
    last_art = Article.objects.all()[:3]
    tags = Tag.objects.all()
    categories = Category.objects.all()
    cat = request.GET.get('cat')
    cat2 = request.GET.get('cat')
    comments = Comment.objects.all()
    q = request.GET.get('q')
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if q:
        articles = articles.filter(title__icontains=q)
    page_num = request.GET.get('page')
    paginator = Paginator(articles, 1)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    ctx = {
        "object_list": page_obj,
        "tags": tags,
        "last_art": last_art,
        "categories": categories,
        'comments': comments,
        'cat2':cat2
    }
    return render(request, 'blogs/articles.html', ctx)


def detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    articles = Article.objects.all()
    last_art = Article.objects.all()[:3]
    tags = Tag.objects.all()
    categories = Category.objects.all()
    cat = request.GET.get('cat')
    comments = Comment.objects.all()
    q = request.GET.get('q')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if not request.user.is_authenticated:
            return redirect("account:login")
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author_id = request.user.profile.id
            obj.article_id = article.id
            obj.save()
            return redirect('.')
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if q:
        articles = articles.filter(title__icontains=q)
    ctx = {
        "object": article,
        "object_list": articles,
        "tags": tags,
        "last_art": last_art,
        "categories": categories,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blogs/blog-single.html', ctx)