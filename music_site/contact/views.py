from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm, SubscribeForm
from podcast.models import Podcast, Tag
from blog.models import Blog


def index(request):
    # footer
    podcasts_footer = Podcast.objects.all()[:3]
    blogs_footer = Blog.objects.all()[:6]
    tagsf = Tag.objects.all()
    # email
    forms = SubscribeForm(request.POST or None)
    if forms.is_valid():
        forms.save()
    # contact
    form = ContactForm()
    if request.method == "POST":
        if request.user.is_authenticated:
            form = ContactForm(data=request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.name = request.user.profile.get_full_name
                obj.save()
                return redirect(".")
        else:
            form = ContactForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect(".")
    ctx = {
        "object_listf": podcasts_footer,  # footer
        "blogs": blogs_footer,  # footer
        "tagsf": tagsf,  # footer
        "form": form,  # contact
        "forms": forms,  # email
    }
    return render(request, 'contact/contact.html', ctx)
