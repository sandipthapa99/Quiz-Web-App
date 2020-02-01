from django.shortcuts import render, redirect
from .models import Resource
from .forms import ResourceForm
from django.db.models import Q
from django.http import HttpResponse, JsonResponse

def upload_resource(request):
	if request.method == "POST":
		form = ResourceForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('resources:resource')
	form = ResourceForm()
	return render(request, "resources/upload.html", {"form": form})


def resource_Page(request):
	resource = Resource.objects.all()
	return render(request, "resources/resourcePage.html", {"resources": resource})







