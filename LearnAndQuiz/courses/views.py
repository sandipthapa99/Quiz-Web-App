from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Course
from .forms import OurForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import admin_only

COURSES_PER_PAGE = 3

def coursePage(request):
	courses = Course.objects.all()
	query = ""
	if request.GET:
		query = request.GET.get('q', '')
		#The empty string handles an empty request
	courses = search(str(query))

	# pagination
	page = request.GET.get('page', 1)#page to show in adress bar
	paginator = Paginator(courses, COURSES_PER_PAGE)
	try:
		courses = paginator.page(page)
	except PageNotAnInteger:
		courses = paginator.page(1)
		#If searched page is not an integer, deliver first page.
	except EmptyPage:
		courses = paginator.page(paginator.num_pages)
		#If searched page is out of range(e.g. 9999), deliver last page.

	return render(request, "courses/courses.html", {"courses" : courses, "query" : query})


def search(query=None):
	queryset = []
	queries = query.split(" ") #allows to search in paragraph
	for q in queries:
		courses = Course.objects.filter(
			Q(title__icontains=q) |
			Q(detail__icontains=q)
			) #case insensitive
		for course in courses:
			queryset.append(course) #adds course into queryset

	return list(set(queryset))


@admin_only #only admin can access this function. Defined in decorators
def delete_course(request, pk):
	course = Course.objects.get(pk=pk)
	course.delete()
	return redirect('courses:courses')

def quiz_info(request, pk=11):
	c = Course.objects.get(pk=pk)
	return render(request, "courses/quizinfo.html", {'courses':c})


#needs to be logged in to get access to these func. If not redirect to login page
@login_required(login_url='/signin/')
def course_java(request):
	return render(request, 'courses/java.html')

@login_required(login_url='/signin/')
def course_python(request):
	return render(request, 'courses/python.html')

@login_required(login_url='/signin/')
def course_html(request):
	return render(request, 'courses/html.html')

@login_required(login_url='/signin/')
def course_php(request):
	return render(request, 'courses/comingsoon.html')

@login_required(login_url='/signin/')
def course_c(request):
	return render(request, 'courses/comingsoon.html')
	