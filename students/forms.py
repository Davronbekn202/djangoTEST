from django import forms
from .models import StudentModel

class BaseForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = [
            'name',
            'age',
            'email',
            'course'
        ]
