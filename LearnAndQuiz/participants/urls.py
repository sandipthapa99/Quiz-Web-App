from django.urls import path
from . import views

app_name="participants"

urlpatterns = [
	path('',views.index, name = 'index'),
	path('signin/', views.signin, name = 'signin'),
	path('signup/', views.signup, name = 'signup'),
	path('logout/', views.logout, name = 'logout'),   
	path('update/', views.update, name = 'update'),
	path('update/done', views.updatedone, name ='updatedone'),
	path('profile/', views.profile, name = 'profile'),
]