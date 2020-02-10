from django.contrib import admin

# Registering models.
from .models import Course

admin.site.register(Course)