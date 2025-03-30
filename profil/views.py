from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, TemplateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, ContactForm
from .models import CustomUser, Course, Lesson, Enrollment, ContactMessage

User = get_user_model()

# Contact Form View
class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Xabaringiz yuborildi!")
        return super().form_valid(form)

# Course List View
class CourseListView(ListView):
    model = Course
    template_name = "courses.html"
    context_object_name = "courses"

    def get_queryset(self):
        level = self.request.GET.get("level")
        return Course.objects.filter(level=level) if level else Course.objects.all()

# Course Detail View
class CourseDetailView(LoginRequiredMixin,DetailView):
    model = Course
    template_name = "course_detail.html"
    context_object_name = "course"
    login_url = reverse_lazy("login") 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lessons"] = self.object.lessons.all()
        context["is_enrolled"] = Enrollment.objects.filter(user=self.request.user, course=self.object).exists()
        return context

# Lesson Detail View
class LessonDetailView(DetailView):
    model = Lesson
    template_name = "lesson_detail.html"
    context_object_name = "lesson"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = self.object.course
        context["lessons"] = Lesson.objects.filter(course=self.object.course)
        return context

# Enroll in Course (Function-Based View)
class EnrollInCourseView(LoginRequiredMixin, View):
    def post(self, request, course_id, *args, **kwargs):
        course = get_object_or_404(Course, id=course_id)
        Enrollment.objects.get_or_create(user=request.user, course=course)
        return redirect(reverse_lazy("course_detail", kwargs={"pk": course.id}))

# User Registration View
class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return self.success_url

# Homepage View
class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.all()
        return context
