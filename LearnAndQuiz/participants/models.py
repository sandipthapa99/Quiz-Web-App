from django.db import models
from courses.models import Course


class Question(models.Model):
	ques = models.TextField()
	correct_ans = models.CharField(max_length = 20)
	title = models.ForeignKey(Course, on_delete = models.CASCADE)

	def __str__(self):
		return self.ques


class Answer(models.Model):
	ans = models.CharField(max_length=20)
	ques = models.ForeignKey(Question, on_delete = models.CASCADE)

	def __str__(self):
		return self.ans
