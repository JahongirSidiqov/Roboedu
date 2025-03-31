from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Course, Lesson, Enrollment, Quiz, Question, Answer, ContactMessage

User = get_user_model()

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword", email="test@example.com")

    def test_create_user(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertTrue(self.user.check_password("testpassword"))

class CourseModelTest(TestCase):
    def setUp(self):
        self.instructor = User.objects.create_user(username="instructor", password="password")
        self.course = Course.objects.create(
            title="Python Course",
            description="Learn Python",
            instructor=self.instructor,
            level="beginner"
        )

    def test_course_creation(self):
        self.assertEqual(self.course.title, "Python Course")
        self.assertEqual(self.course.level, "beginner")

class LessonModelTest(TestCase):
    def setUp(self):
        self.instructor = User.objects.create_user(username="instructor", password="password")
        self.course = Course.objects.create(title="Python Course", description="Learn Python", instructor=self.instructor)
        self.lesson = Lesson.objects.create(course=self.course, title="Lesson 1", content="Introduction")

    def test_lesson_creation(self):
        self.assertEqual(self.lesson.title, "Lesson 1")
        self.assertEqual(self.lesson.course, self.course)

class EnrollmentModelTest(TestCase):
    def setUp(self):
        self.student = User.objects.create_user(username="student", password="password")
        self.instructor = User.objects.create_user(username="instructor", password="password")
        self.course = Course.objects.create(title="Python Course", description="Learn Python", instructor=self.instructor)
        self.enrollment = Enrollment.objects.create(user=self.student, course=self.course)

    def test_enrollment_creation(self):
        self.assertEqual(self.enrollment.user.username, "student")
        self.assertEqual(self.enrollment.course.title, "Python Course")

class QuizModelTest(TestCase):
    def setUp(self):
        self.instructor = User.objects.create_user(username="instructor", password="password")
        self.course = Course.objects.create(title="Python Course", description="Learn Python", instructor=self.instructor)
        self.quiz = Quiz.objects.create(course=self.course, title="Quiz 1")

    def test_quiz_creation(self):
        self.assertEqual(self.quiz.title, "Quiz 1")
        self.assertEqual(self.quiz.course.title, "Python Course")

class QuestionModelTest(TestCase):
    def setUp(self):
        self.instructor = User.objects.create_user(username="instructor", password="password")
        self.course = Course.objects.create(title="Python Course", description="Learn Python", instructor=self.instructor)
        self.quiz = Quiz.objects.create(course=self.course, title="Quiz 1")
        self.question = Question.objects.create(quiz=self.quiz, text="What is Python?")

    def test_question_creation(self):
        self.assertEqual(self.question.text, "What is Python?")
        self.assertEqual(self.question.quiz.title, "Quiz 1")

class AnswerModelTest(TestCase):
    def setUp(self):
        self.instructor = User.objects.create_user(username="instructor", password="password")
        self.course = Course.objects.create(title="Python Course", description="Learn Python", instructor=self.instructor)
        self.quiz = Quiz.objects.create(course=self.course, title="Quiz 1")
        self.question = Question.objects.create(quiz=self.quiz, text="What is Python?")
        self.answer = Answer.objects.create(question=self.question, text="A programming language", is_correct=True)

    def test_answer_creation(self):
        self.assertEqual(self.answer.text, "A programming language")
        self.assertTrue(self.answer.is_correct)

class ContactMessageModelTest(TestCase):
    def setUp(self):
        self.contact_message = ContactMessage.objects.create(name="John Doe", email="john@example.com", message="Hello!")

    def test_contact_message_creation(self):
        self.assertEqual(self.contact_message.name, "John Doe")
        self.assertEqual(self.contact_message.email, "john@example.com")

