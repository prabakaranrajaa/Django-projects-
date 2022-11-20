from django import forms
from crudApp.models import Student

# Create your forms here


class StudentFo(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

# data information
# metadata
