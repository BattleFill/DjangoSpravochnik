from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, VideoCourse
from django.shortcuts import render, get_object_or_404
from .models import Course


def index(request):
    return render(request, 'home/index.html')


def video(request):
    courses = Course.objects.prefetch_related('contents').all()
    video_courses = VideoCourse.objects.all()
    return render(request, 'home/video.html',
    {
        'courses': courses,
        'video_courses': video_courses
    })

def guide(request): 
    courses = Course.objects.prefetch_related('contents').all()
    video_courses = VideoCourse.objects.all()
    return render(request, 'home/guide.html', 
    {
        'courses': courses,
        'video_courses': video_courses
    })


def themes(request):
    courses = Course.objects.prefetch_related('contents').all()
    video_courses = VideoCourse.objects.all()
    return render(request, 'home/themes.html',
    {
        'courses': courses,
        'video_courses': video_courses
    })


# Список всех курсов
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    contents = course.contents.all()  # Получаем все связанные темы
    return render(request, 'home/course_detail.html', {'course': course, 'contents': contents})