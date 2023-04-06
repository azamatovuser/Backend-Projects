from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article, Category, Tag, Comment
from .forms import CommentForm


def index(request):
    articles = Article.objects.order_by('-id')
    page_num = request.GET.get('page')
    paginator = Paginator(articles, 1)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    ctx = {
        'object_list': page_obj
    }
    return render(request, 'blogs/index.html', ctx)


def article_list(request):
    articles = Article.objects.all()
    tag = request.GET.get('tag')
    q = request.GET.get('q')
    cat = request.GET.get('cat')
    if q:
        articles = articles.filter(title__icontains=q)
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    page_num = request.GET.get('page')
    paginator = Paginator(articles, 1)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    ctx = {
        'object_list': page_obj,
    }
    return render(request, 'blogs/blog.html', ctx)


def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    last_3_articles = Article.objects.order_by('id')[:3]
    comments = Comment.objects.all()
    form = CommentForm()
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(".")
        form = CommentForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author_id = request.user.profile.id
            obj.article_id = article.id
            obj.save()
            return redirect('.')
    ctx = {
        'object': article,
        'tags': tags,
        'categories': categories,
        'last_3_articles': last_3_articles,
        'form': form,
        'comments': comments,
    }
    return render(request, 'blogs/blog-single.html', ctx)


def about(request):
    ctx = {

    }
    return render(request, 'blogs/about.html', ctx)