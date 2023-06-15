from django import forms
from app_courses.models import courseModel

class CourseCreateForm(forms.ModelForm):
    class Meta:
        # fields = ("__all__") #for all fields
        fields =("course_name","course_code")
        model = courseModel

