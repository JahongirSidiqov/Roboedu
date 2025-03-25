from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from .forms import CustomUserRegistrationForm
from .models import Course, Lesson
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .models import Course, Lesson, Enrollment

User = get_user_model()
class CourseDetailView(DetailView):
    model = Course
    template_name = "course_detail.html"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lessons"] = self.object.lessons.all()
        context["is_enrolled"] = Enrollment.objects.filter(user=self.request.user, course=self.object).exists()  # Fixed reference
        return context


@login_required
def enroll_in_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)
    return redirect("course_detail", pk=course.id)

class LessonDetailView(DetailView):
    model = Lesson
    template_name = "lesson_detail.html"
    context_object_name = "lesson"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = self.object.course
        context["lessons"] = Lesson.objects.filter(course=self.object.course)
        return context
    
class RegisterView(CreateView):
    model = User
    form_class = CustomUserRegistrationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.all()  # Fetch all courses
        return context
    
