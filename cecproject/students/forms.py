from django import forms
from .models import Student, STATUS_REASON_CHOICES


class StudentForm(forms.ModelForm):
    class Meta:
        model  = Student
        fields = ['first_name', 'last_name', 'age', 'course', 'year_level', 'school_id', 'email', 'profile_picture', 'is_active', 'status_reason']
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
            'school_id': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. CEC2023001',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. student@example.com',
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-file',
                'accept': 'image/*',
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check',
            }),
            'status_reason': forms.Select(attrs={
                'class': 'form-input form-select',
            }),
        }
        labels = {
            'first_name':      'First Name',
            'last_name':       'Last Name',
            'age':             'Age',
            'course':          'Course',
            'year_level':      'Year Level',
            'school_id':       'School ID',
            'email':           'Email (Optional)',
            'profile_picture': 'Profile Picture (Optional)',
            'is_active':       'Active Student',
            'status_reason':   'Status Reason',
        }


class StudentRegistrationForm(forms.ModelForm):
    """Public registration form for students"""
    class Meta:
        model  = Student
        fields = ['first_name', 'last_name', 'age', 'course', 'year_level', 'school_id', 'email', 'profile_picture']
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
            'school_id': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. CEC2023001',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'example@email.com (Optional)',
                'required': False,
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
            'school_id':       'School ID',
            'email':           'Email (Optional)',
            'profile_picture': 'Profile Picture (Optional)',
        }
