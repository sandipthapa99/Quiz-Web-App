from django import forms
from .models import Course


# Our custom form
class OurForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'detail', 'image')
