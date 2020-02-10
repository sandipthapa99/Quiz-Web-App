from django.test import TestCase
from .models import Course
from django.urls import reverse, resolve
from .views import coursePage


class CourseTestCase(TestCase):
	def setUp(self):
		course = Course.objects.create(title="test", detail="this is a test course.")


	def test_data(self):
		course = Course.objects.get(title="test")
		self.assertEqual(course.title, "test") #checking if title is valid, test should be successful

	def test_no_data(self):
		course = Course.objects.get(title="test")
		self.assertEqual(course.title, "") #checking empty title, test should be unsuccessful

	# def test_detail(self):
	# 	course= Course.objects.get(detail="Some words")
	# 	self.assertEqual(course.detail, "Some words")



