from django import forms
from .models import StudentModel

class BaseForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['name', 'age', 'email', 'course']

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError("you must be older than 18")
        return age

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("name can't be number")
        return name