from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Course
from django.core.paginator import Paginator


# def coursePage(request):
# 	courses = Course.objects.all()
# 	return render(request, "courses/courses.html", {"courses": courses})


COURSES_PER_PAGE = 3
def coursePage(request):
	courses = Course.objects.all()
	query = ""
	if request.GET:
		query = request.GET.get('q', '')
	courses = search(str(query))

	# pagination
	page = request.GET.get('page', 1)
	course_paginator = Paginator(courses, COURSES_PER_PAGE)
	courses= course_paginator.page(page)

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




#n
