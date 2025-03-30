from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomePageView,EnrollInCourseView, RegisterView, CourseDetailView, LessonDetailView, CourseListView, ContactView, CustomLoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('', HomePageView.as_view(), name='index'),
    path("course/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),
    path("courses/", CourseListView.as_view(), name="courses"),
    path("courses/<int:course_id>/enroll/", EnrollInCourseView.as_view(), name="enroll_in_course"),
    path("lesson/<int:pk>/", LessonDetailView.as_view(), name="lesson_detail"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('contact/', ContactView.as_view(), name='contact'),

]
# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)