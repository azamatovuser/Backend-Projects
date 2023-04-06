from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Blog, Category, Tag1
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from podcast.models import Podcast, Tag
from datetime import datetime, timedelta
from .models import Blog, Comment_blog
from .forms import CommentForm


def index(request):
    podcasts_footer = Podcast.objects.all()[:3]
    blogs_footer = Blog.objects.all()[:6]
    tagsf = Tag.objects.all()
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    tags1 = Tag1.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    q = request.GET.get('q')
    if q:
        blogs = blogs.filter(title__icontains=q)
    if cat:
        blogs = blogs.filter(category__title__exact=cat)
    if tag:
        blogs = blogs.filter(tags__title__exact=tag)
    page_num = request.GET.get('page')
    paginator = Paginator(blogs, 3)
    try:
        page_obj = paginator.page(page_num)
    except EmptyPage:
        page_obj = paginator.page(1)
    except InvalidPage:
        page_obj = paginator.page(1)
    ctx = {
        "object_list": page_obj,
        'categories': categories,
        'tags': tags1,
        "object_listf": podcasts_footer,
        'blogs': blogs_footer,
        "tagsf": tagsf
    }
    return render(request, 'blog/blog.html', ctx)


def archive(request, pk):
    podcasts_footer = Podcast.objects.all()[:3]
    blogs_footer = Blog.objects.all()[:6]
    tagsf = Tag.objects.all()
    articles = Blog.objects.all()
    categories = Category.objects.all()
    tags1 = Tag1.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    q = request.GET.get('q')
    if pk == 1:
        now = datetime.now() - timedelta(minutes=60*24)
        articles = articles.filter(created_date__gte=now)
    if pk == 2:
        now = datetime.now() - timedelta(minutes=60*24*7)
        articles = articles.filter(created_date__gte=now)
    if pk == 3:
        now = datetime.now() - timedelta(minutes=60*24*30)
        articles = articles.filter(created_date__gte=now)
    if pk == 4:
        now = datetime.now() - timedelta(minutes=60*24*360)
        articles = articles.filter(created_date__gte=now)
    if q:
        articles = articles.filter(title__icontains=q)
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    page_num = request.GET.get('page')
    paginator = Paginator(articles, 3)
    try:
        page_obj = paginator.page(page_num)
    except EmptyPage:
        page_obj = paginator.page(1)
    except InvalidPage:
        page_obj = paginator.page(1)
    ctx = {
        "object_list": page_obj,
        "object_listf": podcasts_footer,
        'blogs': blogs_footer,
        "tagsf": tagsf,
        'categories': categories,
        'tags': tags1,
    }
    return render(request, 'blog/blog.html', ctx)


def detail(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    podcasts_footer = Podcast.objects.all()[:3]
    blogs_footer = Blog.objects.all()[:6]
    tags1 = Tag1.objects.all()
    tagsf = Tag.objects.all()
    categories = Category.objects.all()
    comments = Comment_blog.objects.all()
    form = CommentForm(request.POST or None)
    if form.is_valid():
        if not request.user.is_authenticated:
            return redirect("account:login")
        obj = form.save(commit=False)
        obj.author = request.user.profile
        obj.podcast = blog
        obj.save()
        return redirect(".")
    ctx = {
        'object': blog,
        "tags1": tags1,
        "tagsf": tagsf,
        "cats": categories,
        "comments": comments,
        'form': form,
        'object_listf': podcasts_footer,
        'blogs': blogs_footer,
    }
    return render(request, 'blog/detail.html', ctx)