from django.test import TestCase
from .models import Question

class QuestionTestCase(TestCase):

	def setUp(self):
	def test_valid_question(self):
		question=Question.objects.create(ques="some question", correct_ans="some answer")
		self.assertTrue(question.is_valid_question())
