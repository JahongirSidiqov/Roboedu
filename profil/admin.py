from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_student', 'is_instructor', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    list_filter = ('is_student', 'is_instructor', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)

from .models import Course, Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'created_at')
    search_fields = ('title', 'instructor__username')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'created_at')
    search_fields = ('title', 'course__title')


