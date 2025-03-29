from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_student', 'is_instructor', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    list_filter = ('is_student', 'is_instructor', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)

from .models import Course, Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor','level', 'created_at')
    search_fields = ('title', 'instructor__username','level')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'created_at')
    search_fields = ('title', 'course__title')


