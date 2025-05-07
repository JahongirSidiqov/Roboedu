from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    HomePageView, EnrollInCourseView, RegisterView, CourseDetailView, 
    LessonDetailView, CourseListView, ContactView, CustomLoginView
)
from django.conf import settings
from django.conf.urls.static import static

# URL patterns for different views in the application
urlpatterns = [
    # Home Page
    path('', HomePageView.as_view(), name='index'),  # Displays the homepage

    # Course-related URLs
    path("course/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),  # Shows details of a specific course
    path("courses/", CourseListView.as_view(), name="courses"),  # Lists all available courses
    path("courses/<int:course_id>/enroll/", EnrollInCourseView.as_view(), name="enroll_in_course"),  # Enrolls a user in a course

    # Lesson-related URLs
    path("lesson/<int:pk>/", LessonDetailView.as_view(), name="lesson_detail"),  # Displays lesson details

    # Authentication URLs
    path("register/", RegisterView.as_view(), name="register"),  # User registration page
    path("login/", CustomLoginView.as_view(template_name="registration/login.html"), name="login"),  # User login page
    path("logout/", LogoutView.as_view(), name="logout"),  # Logs out the user

    # Contact page
    path('contact/', ContactView.as_view(), name='contact'),  # Contact form for users

]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])