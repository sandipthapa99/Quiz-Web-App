from django.contrib import admin

# Register your models here.
from .models import Question, Answer
from .models import Profile

admin.site.register(Profile)

admin.site.register(Question)
admin.site.register(Answer)
