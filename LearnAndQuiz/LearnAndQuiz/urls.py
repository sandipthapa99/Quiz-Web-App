
from django.contrib import admin
from django.urls import path, include
from django.conf import settings#setting within same folder
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('participants.urls')),
    path('',include('courses.urls')),
    path('',include('question.urls')),
    path('',include('resources.urls')),
    path('',include('restapi.urls')),
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)