from django.urls import path, include
from . import views

app_name = 'question'

urlpatterns = [
    path('question/', views.question, name = 'question'),
    path('question/<pk>/', views.question, name = 'question'),
   # path('question/<pk>/<qpk>', views.question, name = 'question')
    
]
