from django import forms
from .models import Course

class OurForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'detail', 'image')
