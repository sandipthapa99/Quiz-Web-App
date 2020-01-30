from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Q
from .models import Course
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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




def read_api(request):
	course = Course.objects.all()
	dict_value = {"course":list(course.values('title', 'detail'))}
	return JsonResponse(dict_value)

@csrf_exempt
def update_api(request, pk):
	course = Course.objects.get(pk = pk)
	if request.method == "GET":
		return JsonResponse({"title":course.title, "detail":course.detail})

	else:
		decoded_data = request.body.decode('utf-8')
		course_data = json.loads(decoded_data)
		course.title = course_data['title']
		course.detail = course_data['detail']
		course.save()
		return JsonResponse({"message": "Successfully updated"})

def delete_data(request, pk):
	course = Course.objects.get(pk = pk)
	course.delete()
	return redirect('courses:courses')


def update_data(request, pk):
	instance = get_object_or_404(Course, id=pk)
	form = OurForm()
	if request.method == "POST":
		form = OurForm(request.POST, reques.FILES, instance)
		if form.is_valid():
			form.save()
			return redirect('courses:courses')

	return render(request, 'courses/courses.html', {'courses': instance})