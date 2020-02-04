from django.urls import path
from . import views

app_name="resources"

urlpatterns = [
	path('resources/', views.resource_Page, name ="resource"),
	path('resources/upload/', views.upload_resource, name ="upload"),
	path('download/', views.download_line, name ="download"),

]