from django import forms
from app_students.models import studentModel

class StudentCreateForm(forms.ModelForm):
    class Meta:
        fields=("first_name","middle_name","last_name","email","profile_img","contact","address","course","current_degree")
        model= studentModel


