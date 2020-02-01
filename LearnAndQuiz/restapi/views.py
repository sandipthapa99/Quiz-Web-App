from django.shortcuts import render,redirect, get_object_or_404
from courses.models import Course
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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



# def pagination(request, PAGENO, SIZE):
# 	skip = SIZE* (PAGENO -1)
# 	courses = Course.objects.all() [skip:(PAGENO * SIZE)]
# 	dict = {
# 	"courses":list(Course.values("title", "name"))
# 	}
# 	return JsonResponse(dict)