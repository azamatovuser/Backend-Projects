from django.shortcuts import render, redirect, get_object_or_404, Http404, reverse
from apps.blog.models import Post, Body, Comment, Category, Tag
from apps.course.models import Course
from apps.main.v1.forms import SubscribeForm
from .forms import CommentForm
from django.views import generic


class BlogView(generic.ListView):
    template_name = 'blog/blog.html'
    queryset = Post.objects.all()
    paginate_by = 1

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data()
        ctx['courses'] = Course.objects.order_by('-id')[:3]
        ctx['categories'] = Category.objects.all()
        ctx['tags'] = Tag.objects.all()
        return ctx


class BlogDetailView(generic.View):
    template_name = 'blog/blog-single.html'
    queryset = Post.objects.all()

    def get_object(self, request, pk):
        try:
            post = self.queryset.get(id=pk)
        except Post.DoesnotExist:
            raise Http404
        return post

    def get_context_data(self, request, pk):
        ctx = {'object': self.get_object(request, pk),
               'categories': Category.objects.all(),
               'tags': Tag.objects.all,
               'courses': Course.objects.order_by('-id')[:3],
               }
        return ctx

    def get(self, request, pk, *args, **kwargs):
        ctx = self.get_context_data(request, pk)
        comments = Comment.objects.filter(post_id=pk, parent_comment__isnull=True)
        ctx['comments'] = comments
        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        if not request.user.is_authenticated:
            return redirect("account:login")

        comment_id = request.GET.get('comment_id', None)
        user_id = request.user.id
        body = request.POST.get('body', None)
        if body:
            obj = Comment.objects.create(author_id=user_id, post_id=pk, body=body, parent_comment_id=comment_id)
            return redirect(reverse('blog:blog-single', kwargs={'pk': pk}) + '#comments')
        return render(request, self.template_name, ctx)

#
# def blog(request):
#     posts = Post.objects.all()
#     last_three_courses = Course.objects.all()
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
#     forms = SubscribeForm()
#     if request.method == "POST":
#         forms = SubscribeForm(data=request.POST)
#         if forms.is_valid():
#             forms.save()
#             return redirect('.')
#     ctx = {
#         'posts': posts,
#         'courses': last_three_courses,
#         'categories': categories,
#         'tags': tags,
#         'forms': forms
#     }
#     return render(request, 'blog/blog.html', ctx)
#
#
# def blog_single(request, pk):
#     post = get_object_or_404(Post, id=pk)
#     categories = Category.objects.all()
#     last_three_courses = Course.objects.all()
#     tags = Tag.objects.all()
#     forms = SubscribeForm()
#     if request.method == "POST":
#         forms = SubscribeForm(data=request.POST)
#         if forms.is_valid():
#             forms.save()
#             return redirect('.')
#     ctx = {
#         'post': post,
#         'courses': last_three_courses,
#         'categories': categories,
#         'tags': tags,
#         'forms': forms
#     }
#     return render(request, 'blog/blog-single.html', ctx)
