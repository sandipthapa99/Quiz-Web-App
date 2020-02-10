from django.urls import path, include
from . import views
from django.conf.urls import url
app_name = 'customquiz'

urlpatterns = [
    path('customquiz/', views.addquiz, name = 'addquiz'),
    path('customquiz/', views.addques, name = 'addques'),
    path('customquiz/addques/<int:pk>/', views.addques, name = 'addques'),
   	path('customquiz/showques/<int:pk>', views.showques, name = 'showques'),
   	path('customquiz/editques/<int:pk>', views.editques, name = 'editques'),
   	path('customquiz/edittitle/<int:pk>', views.edittitle, name = 'edittitle'),
   	path('customquiz/deleteques/<int:pk>', views.deleteques, name = 'deleteques'),

]
