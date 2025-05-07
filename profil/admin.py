from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Course, Lesson, Quiz, Question, Answer, ContactMessage, Enrollment

# Registering CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_student', 'is_instructor', 'is_staff', 'is_superuser','bio','image')
    search_fields = ('username', 'email')
    list_filter = ('is_student', 'is_instructor', 'is_staff')

# Registering Course
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'level', 'duration', 'project_count', 'created_at')
    search_fields = ('title', 'instructor__username', 'level')

# Registering Lesson
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'created_at')
    search_fields = ('title', 'course__title')

# Registering Enrollment
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at')
    search_fields = ('user__username', 'course__title')

# Registering Quiz
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'created_at')
    search_fields = ('title', 'course__title')

# Registering Questions with Inline Answers
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz')
    search_fields = ('text', 'quiz__title')
    inlines = [AnswerInline]  # Inline answers inside QuestionAdmin

# Registering Answer
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    search_fields = ('text', 'question__text')

# Registering Contact Messages
@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
