from django.contrib import admin
from django.urls import path
from . import views

app_name="courses"

urlpatterns = [
	path('courses/', views.coursePage, name = 'courses'),
	]