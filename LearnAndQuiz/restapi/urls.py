from django.contrib import admin
from django.urls import path
from . import views

app_name="restapi"

urlpatterns = [
	path('api/', views.read_api, name = 'read_api'),
	path('api/update/<int:pk>/', views.update_api, name = 'update_api'),
	path('api/delete/<int:pk>/', views.delete_data, name = 'delete_data'),
	path('api/<int:PAGENO>/<int:SIZE>/', views.pagination, name = 'pagination'),

]