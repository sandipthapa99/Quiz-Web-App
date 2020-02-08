from django.shortcuts import render, redirect
from participants.models import Question, Answer
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

sindex = 0
eindex = 1
score = 0
	
def question(request, pk="1", qpk=1):
	if request.method == 'POST':
		chosen = request.POST['choice']
		global sindex
		global eindex
		global score
		q = Question.objects.filter(title_id = pk)[sindex:eindex].get()
		if str(chosen) == q.correct_ans:
				score += 10
				
		while eindex < Question.objects.filter(title_id = pk).count():		
			sindex +=1
			eindex +=1
			q = Question.objects.filter(title_id = pk)[sindex:eindex].get()	
			a = Answer.objects.filter(ques_id = q.pk)
			return render(request, 'question/question.html', context ={'question':q, 'answer':a})
			
		else:
			return HttpResponse("The quiz is over!<br> Your score is {}".format(score))

	else:
		sindex = 0
		eindex = 1
		score = 0
		q = Question.objects.filter(title_id = pk)[sindex:eindex].get()
		a = Answer.objects.filter(ques_id = q.pk)
		return render(request, 'question/question.html', context ={'question':q, 'answer':a})












