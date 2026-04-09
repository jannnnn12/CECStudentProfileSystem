from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model  = Student
        fields = ['first_name', 'last_name', 'age', 'course', 'year_level', 'profile_picture']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. Juan',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. Dela Cruz',
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. 20',
                'min': 15,
                'max': 60,
            }),
            'course': forms.Select(attrs={
                'class': 'form-input form-select',
            }),
            'year_level': forms.Select(attrs={
                'class': 'form-input form-select',
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-file',
                'accept': 'image/*',
            }),
        }
        labels = {
            'first_name':      'First Name',
            'last_name':       'Last Name',
            'age':             'Age',
            'course':          'Course',
            'year_level':      'Year Level',
            'profile_picture': 'Profile Picture',
        }
