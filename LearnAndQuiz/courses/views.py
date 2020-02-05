from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Course
from .forms import OurForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import Group
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
	queries = query.split(" ")
	for q in queries:
		courses = Course.objects.filter(
			Q(title__icontains=q) |
			Q(detail__icontains=q)
			)
		for course in courses:
			queryset.append(course)

	return list(set(queryset))




#pagination
def pagination(request, PAGENO, SIZE):
	skip= SIZE * (PAGENO -1)
	courses = Course.objects.all() [skip:(PAGENO * SIZE)]
	dict = {
	"courses":list(Course.values("title", "detail"))
	}
	return JsonResponse(dict)

@admin_only
def delete_course(request, pk):
	course = Course.objects.get(pk=pk)
	course.delete()
	return redirect('courses:courses')