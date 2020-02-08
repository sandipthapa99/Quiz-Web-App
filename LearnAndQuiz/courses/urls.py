from django.contrib import admin
from django.urls import path
from . import views

app_name="courses"

urlpatterns = [
	path('courses/', views.coursePage, name = 'courses'),
	path('courses/delete/<int:pk>/', views.delete_course, name='delete_course'),
	path('courses/java/', views.course_java, name = 'java'),
	
]