from django import forms
from participants.models import Question, Answer
from courses.models import Course

class course_form(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['title', 'detail', 'image']

class question_form(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['ques','correct_ans','title']

class answer_form(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['ans', 'ques']
