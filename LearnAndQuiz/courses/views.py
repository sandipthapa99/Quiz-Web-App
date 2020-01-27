from django.shortcuts import render
from django.db.models import Q
from .models import Course

# def coursePage(request):
# 	courses = Course.objects.all()
# 	return render(request, "courses/courses.html", {"courses": courses})

def coursePage(request):
	courses = Course.objects.all()
	query = ""
	if request.GET:
		query = request.GET['q']
	courses = search(str(query))
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




