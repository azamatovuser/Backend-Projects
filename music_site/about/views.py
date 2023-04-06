from django.shortcuts import render
from contact.forms import SubscribeForm
from podcast.models import Podcast, Tag
from blog.models import Blog
from podcast.models import Podcast, Like


def index(request):
    podcast_count = Podcast.objects.all().count()
    blog_count = Blog.objects.all().count()
    like_count = Like.objects.all().count()
    podcasts_footer = Podcast.objects.all()[:3]
    blogs_footer = Blog.objects.all()[:6]
    tags = Tag.objects.all()
    forms = SubscribeForm(request.POST or None)
    if forms.is_valid():
        forms.save()
    ctx = {
        "podcast_count": podcast_count,
        "blog_count": blog_count,
        "like_count": like_count,
        "object_listf": podcasts_footer,
        "blogs": blogs_footer,
        "tagsf": tags,
        "forms": forms
    }
    return render(request, 'about/about.html', ctx)