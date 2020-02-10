from django.contrib import admin
from django.urls import path
from . import views

app_name="courses"

urlpatterns = [
	path('courses/', views.coursePage, name = 'courses'),
	path('courses/delete/<int:pk>/', views.delete_course, name='delete_course'),
	path('courses/java/', views.course_java, name = 'java'),
	path('courses/python/', views.course_python, name = 'python'),
	path('courses/html/', views.course_html, name = 'html'),
	path('courses/php/', views.course_php, name = 'php'),
	path('courses/c++/', views.course_c, name = 'c'),
	path('courses/<int:pk>', views.quiz_info, name = 'quizinfo'),
	
]