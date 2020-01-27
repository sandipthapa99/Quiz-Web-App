from django.shortcuts import render
from participants.models import Question, Answer
from django.http import HttpResponse
# Create your views here.
def question(request, pk="1"):
	if request.method == 'POST':
		chosen = request.POST['choice']
		q = Question.objects.get(pk = pk)
		if str(chosen) == q.correct_ans:
			return HttpResponse('Correct answer')

		else:
			return HttpResponse('Incorrect answer')

	else:
		q = Question.objects.get(pk = pk)
		a = Answer.objects.filter(ques_id = pk)
		
		return render(request, 'question/question.html', context ={'question':q, 'answer':a})
