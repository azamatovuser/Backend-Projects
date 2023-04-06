from django.shortcuts import render
from blogs.models import Article, Category, Tag, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def about(request):
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
    return render(request, 'blogs/about.html', ctx)