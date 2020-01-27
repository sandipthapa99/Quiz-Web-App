from django.urls import path, include
from . import views

urlpatterns = [
    path('question/', views.question, name = 'question'),
    path('question/<int:pk>', views.question, name = 'question'),


]
