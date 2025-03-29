from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.views.generic import TemplateView, DetailView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Lesson, Enrollment
from django.views.generic import ListView
from django import forms
from .models import ContactMessage
from django.contrib.auth.views import LoginView
User = get_user_model()

from django.views.generic.edit import FormView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import ContactMessage

class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Xabaringiz yuborildi!")
        return super().form_valid(form)

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class CourseListView(ListView):
    model = Course
    template_name = "courses.html"  # Template file
    context_object_name = "courses"  # Variable name in template
    def get_queryset(self):
        level = self.request.GET.get("level")  # Get level from URL query
        if level:
            return Course.objects.filter(level=level)
        return Course.objects.all()


class CourseDetailView(DetailView):
    model = Course
    template_name = "course_detail.html"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lessons"] = self.object.lessons.all()
        context["is_enrolled"] = Enrollment.objects.filter(user=self.request.user, course=self.object).exists()  
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
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  # Redirect already logged-in users
    success_url = reverse_lazy('index')  # Redirect after successful login

    def get_success_url(self):
        return self.success_url

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.all()  # Fetch all courses
        return context
    
