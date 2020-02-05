from django.test import TestCase
from .models import Course


class CourseTestCase(TestCase):
	def setUp(self):
		course = Course.objects.create(title="test", detail="this is a test course.")


	def test_data(self):
		course = Course.objects.get(title="test")
		self.assertEqual(course.title, "test")