from django.shortcuts import render,redirect, get_object_or_404
from courses.models import Course
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def read_api(request):
	course = Course.objects.all()
	dictionary = {"course":list(course.values('title', 'detail'))}
	return JsonResponse(dictionary)

@csrf_exempt #bypassing csrf verification. Used to customize views
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
@csrf_exempt
def delete_data(request, pk):
	course = Course.objects.get(pk = pk)
	course.delete()
	return redirect('courses:courses')

#pagination
def pagination(request, PAGENO, SIZE):
	skip = SIZE* (PAGENO -1)
	courses = Course.objects.all() [skip:(PAGENO * SIZE)]
	dict = {
	"courses":list(courses.values("title", "detail"))
	}
	return JsonResponse(dict)