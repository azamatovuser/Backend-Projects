from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Podcast, Category, Tag, Comment, Like, Season
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from blog.models import Blog
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt


def index(request):
    podcasts_footer = Podcast.objects.all()[:3]
    podcasts = Podcast.objects.all()[:3]
    blogs = Blog.objects.all()[:6]
    cats = Category.objects.all()
    tags = Tag.objects.all()
    tagsf = Tag.objects.all()
    try:
        user_id = request.user.profile.id
    except:
        user_id = None
    my_liked_musics = Like.objects.filter(author_id=user_id).values_list('music_id')
    my_liked_musics_list = [i[0] for i in my_liked_musics]
    ctx = {
        "object_list": podcasts,
        "object_listf": podcasts_footer,
        "cats": cats,
        "tags": tags,
        "tagsf": tagsf,
        "blogs": blogs,
        'my_liked_musics_list': my_liked_musics_list
    }
    return render(request, 'podcast/index.html', ctx)


def list(request):
    podcasts_footer = Podcast.objects.all()[:3]
    blogs_footer = Blog.objects.all()[:6]
    podcasts = Podcast.objects.all()
    tags = Tag.objects.all()
    tagsf = Tag.objects.all()
    categories = Category.objects.all()
    try:
        user_id = request.user.profile.id
    except:
        user_id = None
    my_liked_musics = Like.objects.filter(author_id=user_id).values_list('music_id')
    my_liked_musics_list = [i[0] for i in my_liked_musics]
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    q = request.GET.get('q')
    if tag:
        podcasts = podcasts.filter(tag__title__exact=tag)
    if cat:
        podcasts = podcasts.filter(category__title__exact=cat)
    if q:
        podcasts = podcasts.filter(title__icontains=q)
    seasons = Season.objects.all()
    page_num = request.GET.get('page')
    paginator = Paginator(podcasts, 3)
    try:
        page_obj = paginator.page(page_num)
    except EmptyPage:
        page_obj = paginator.page(1)
    except InvalidPage:
        page_obj = paginator.page(1)
    ctx = {
        "object_list": page_obj,
        "tags": tags,
        "tagsf": tagsf,
        'categories': categories,
        "seasons": seasons,
        "object_listf": podcasts_footer,
        "blogs": blogs_footer,
        'my_liked_musics_list': my_liked_musics_list
    }
    return render(request, 'podcast/episodes.html', ctx)


def detail(request, pk):
    podcasts_footer = Podcast.objects.all()[:3]
    blogs_footer = Blog.objects.all()[:6]
    podcast = get_object_or_404(Podcast, id=pk)
    tags = Tag.objects.all()
    tagsf = Tag.objects.all()
    categories = Category.objects.all()
    comments = Comment.objects.all()
    form = CommentForm(request.POST or None)
    if form.is_valid():
        if not request.user.is_authenticated:
            return redirect("account:login")
        obj = form.save(commit=False)
        obj.author = request.user.profile
        obj.podcast = podcast
        obj.save()
        return redirect('.')
    ctx = {
        'object': podcast,
        "tags": tags,
        "tagsf": tagsf,
        "cats": categories,
        "comments": comments,
        'form': form,
        'object_listf': podcasts_footer,
        'blogs': blogs_footer,
    }
    return render(request, 'podcast/episode.html', ctx)


@csrf_exempt
def like(request):
    if not request.user.is_authenticated:
        return JsonResponse({"detail": "Log in !!!"}, status=401)
    if request.method == "POST":
        music_id = int(request.POST.get('music_id'))
        user_id = request.user.profile.id
        likes = Like.objects.values_list('music_id', 'author_id')
        if (music_id, user_id) in likes:
            Like.objects.get(music_id=music_id, author_id=user_id).delete()
            return JsonResponse({"detail": "Un-liked"})
        Like.objects.create(music_id=music_id, author_id=user_id)
        return JsonResponse({"detail": "Liked"})
    return JsonResponse({"detail": "Method not allowed!"})


# def music_ids_list(request):
#     ids_list = [i.id for i in Podcast.objects.all()]
#     return JsonResponse({"ids_list": ids_list})


def ids_list(request):
    musics = Podcast.objects.all().order_by('-id')
    ids_list = [i.id for i in musics]
    return JsonResponse({"ids_list": ids_list})


def archive(request, pk):
    podcasts_footer = Podcast.objects.all()[:3]
    blogs_footer = Blog.objects.all()[:6]
    tagsf = Tag.objects.all()
    podcasts = Podcast.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    q = request.GET.get('q')
    if pk == 1:
        now = datetime.now() - timedelta(minutes=60*24)
        podcasts = podcasts.filter(created_date__gte=now)
    if pk == 2:
        now = datetime.now() - timedelta(minutes=60*24*7)
        podcasts = podcasts.filter(created_date__gte=now)
    if pk == 3:
        now = datetime.now() - timedelta(minutes=60*24*30)
        podcasts = podcasts.filter(created_date__gte=now)
    if pk == 4:
        now = datetime.now() - timedelta(minutes=60*24*360)
        podcasts = podcasts.filter(created_date__gte=now)
    if q:
        podcasts = podcasts.filter(title__icontains=q)
    if cat:
        podcasts = podcasts.filter(category__title__exact=cat)
    if tag:
        podcasts = podcasts.filter(tags__title__exact=tag)
    seasons = Season.objects.all()
    page_num = request.GET.get('page')
    paginator = Paginator(podcasts, 3)
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
        "seasons": seasons,
        "tagsf": tagsf,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'podcast/episodes.html', ctx)