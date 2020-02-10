from django.contrib import messages
from django.shortcuts import render, redirect
from participants.models import Question, Answer
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

sindex = 0 #Index for the slicing of the question objects filter object
eindex = 1
score = 0 #INitial score of the participant
@login_required(login_url="/signin/")
def question(request, pk="1", qpk=1):
	if request.method == 'POST':
		try:
			chosen = request.POST['choice']
			global sindex
			global eindex
			global score
			q = Question.objects.filter(title_id = pk)[sindex:eindex].get()
			if str(chosen) == q.correct_ans: #add score if the chosen answer is correct
					score += 10
					
			while eindex < Question.objects.filter(title_id = pk).count():	 #only run the loop until all the questions in the given topic have been shown.	
				sindex +=1   #add the sindex and eindex after each iteration
				eindex +=1
				q = Question.objects.filter(title_id = pk)[sindex:eindex].get()	#get method to get only 1 element from the queryset
				a = Answer.objects.filter(ques_id = q.pk)
				return render(request, 'question/question.html', context ={'question':q, 'answer':a, 's':score})
				
			else:
				return render(request, 'question/score.html', context={'s':score})
		except:
			messages.info(request, 'Please select your answer!')
			return HttpResponseRedirect("")

	else:
		sindex = 0
		eindex = 1
		score = 0
		try:
			q = Question.objects.filter(title_id = pk)[sindex:eindex].get() #get method to get only 1 element from the queryset
			a = Answer.objects.filter(ques_id = q.pk)
			return render(request, 'question/question.html', context ={'question':q, 'answer':a})
		except:
			return HttpResponse('Sorry, No question has yet been added to the given Course!')












