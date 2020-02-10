from django.shortcuts import render, redirect
from courses.models import Course
from django.contrib import messages
from participants.models import Question, Answer
from .forms import course_form, question_form, answer_form
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse, HttpResponseRedirect, HttpResponse
# Create your views here.
def addquiz(request):
	if request.method == 'POST':
		title = request.POST['title']
		detail = request.POST['detail']
		image = request.FILES['image']

		if Course.objects.filter(title=title).exists():
			messages.info(request, 'Sorry! The course name is already taken!')
			return redirect('customquiz:addquiz')

		else:
			course = Course(title = title, detail = "Custom Quiz", image = image)
			course.save()			
			messages.info(request, 'Title added! Now add some questions for the title.')
			t = Course.objects.get(title = title)
			return render(request, 'customquiz/addques.html', context = {'topic':t})	
	else:

		return render(request, 'customquiz/addquiz.html')


def addques(request, pk):
	if request.method == 'POST':
		t = Course.objects.get(pk = pk)
		ques = request.POST['question']
		corrans = request.POST['correct_ans']
		ans1 = request.POST['opt1']
		ans2 = request.POST['opt2']
		ans3 = request.POST['opt3']
		ans4 = request.POST['opt4']

		if ans1 == corrans or ans2 == corrans or ans3 == corrans or ans4 == corrans:
			ques = Question(ques = ques, correct_ans = corrans, title_id = pk)
			a1 = Answer(ans = ans1, ques = ques)
			a2 = Answer(ans = ans2, ques = ques)
			a3 = Answer(ans = ans3, ques = ques)
			a4 = Answer(ans = ans4, ques = ques)
			ques.save()
			a1.save()
			a2.save()
			a3.save()
			a4.save()
			messages.info(request, 'Question added!')
			return render(request, 'customquiz/addques.html', context = {'topic':t})

		else:	
			messages.info(request, 'You have to specify at least 1 option as the correct answer!')
			return HttpResponseRedirect("")

	else:
		t = Course.objects.get(pk = pk)
		return render(request, 'customquiz/addques.html', context = {'topic':t})


def showques(request, pk):
	title = Course.objects.get(pk=pk)
	questions = Question.objects.filter(title_id=pk)
	return render(request, 'customquiz/showques.html', context={'question':questions, 'course':title})

def edittitle(request,pk):
	if request.method == 'POST':
		pass

	else:
		question = Question.objects.get(pk = pk)
		return render(request, 'customquiz/edittitle.html', context={'question':question})	

def editques(request, pk):
	if request.method == 'POST':		
		q = Question.objects.get(pk=pk)
		a1 = Answer.objects.filter(ques_id = pk)[0:1].get()
		a2 = Answer.objects.filter(ques_id = pk)[1:2].get()
		a3 = Answer.objects.filter(ques_id = pk)[2:3].get()
		a4 = Answer.objects.filter(ques_id = pk)[3:4].get()

		q.ques = request.POST['newques']
		a1.ans = str(request.POST.getlist('newans')[0:1])
		a2.ans = str(request.POST.getlist('newans')[1:2])
		a3.ans = str(request.POST.getlist('newans')[2:3])
		a4.ans = str(request.POST.getlist('newans')[3:4])
		q.save()
		a1.save()
		a2.save()
		a3.save()
		a4.save()
		return HttpResponse('The answers for {} have been saved as {},{},{},{}'.format(q.ques,a1.ans,a2.ans,a3.ans,a4.ans))

	else:
		questions = Question.objects.get(pk=pk)
		answers = Answer.objects.filter(ques_id = pk)
		return render(request, 'customquiz/editques.html', context={'question':questions, 'answers':answers})