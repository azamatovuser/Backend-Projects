from django.shortcuts import render, redirect, reverse, Http404
from apps.course.models import Course, Lesson, LessonFiles, Category, Tag
from apps.main.v1.forms import SubscribeForm
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def course(request):
    courses = Course.objects.all()
    last_three_courses = Course.objects.all()[:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    forms = SubscribeForm()
    if request.method == "POST":
        forms = SubscribeForm(data=request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('.')
    page_num = request.GET.get('page')
    paginator = Paginator(courses, 1)
    try:
        page_obj = paginator.page(page_num)
    except EmptyPage:
        page_obj = paginator.page(1)
    except InvalidPage:
        page_obj = paginator.page(1)
    ctx = {
        'courses': page_obj,
        'last_three': last_three_courses,
        'categories': categories,
        'tags': tags,
        'forms': forms
    }
    return render(request, 'course/courses.html', ctx)


class CourseDetailView(generic.View):
    template_name = 'course/course-single.html'
    queryset = Course.objects.all()

    def get_object(self, request, pk):
        try:
            post = self.queryset.get(id=pk)
        except Course.DoesNotExist:
            raise Http404
        return post

    def get_context_data(self, request, pk, **kwargs):
        ctx = {
            'object': self.get_object(request, pk),
            'categories': Category.objects.all(),
            'tags': Tag.objects.all,
            'courses': Course.objects.order_by('-id')[:3],
            'random_courses': Course.objects.order_by('?')[:6]
        }
        return ctx

    def get(self, request, pk, *args, **kwargs):
        ctx = self.get_context_data(request, pk, **kwargs)
        return render(request, self.template_name, ctx)


def lesson_detail(request, course_id, pk):
    lessons = Lesson.objects.get(id=pk)
    course = Course.objects.get(id=course_id)
    lesson_files = LessonFiles.objects.all()
    main_lesson = LessonFiles.objects.filter(lesson_id=pk, is_main=True).first()
    ctx = {
        'lessons': lessons,
        'course': course,
        'main_lesson': main_lesson,
        'lesson_files': lesson_files
    }
    return render(request, 'course/lesson_detail.html', ctx)