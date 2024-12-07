from django.contrib import admin
from .models import Course, CourseContent, VideoCourse

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "color")

@admin.register(CourseContent)
class CourseContentAdmin(admin.ModelAdmin):
    list_display = ("topic", "course")

@admin.register(VideoCourse)
class VideoCourseAdmin(admin.ModelAdmin):
    list_display = ("title", "color")