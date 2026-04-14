from django import forms
from .models import Student, STATUS_REASON_CHOICES


class StudentForm(forms.ModelForm):
    def clean_school_id(self):
        school_id = (self.cleaned_data.get('school_id') or '').strip()
        if not school_id:
            return school_id

        qs = Student.objects.filter(school_id__iexact=school_id)
        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError("This School ID is already registered. Please use a different School ID.")
        return school_id

    def clean(self):
        cleaned = super().clean()
        first_name = (cleaned.get('first_name') or '').strip()
        last_name = (cleaned.get('last_name') or '').strip()
        course = cleaned.get('course')
        year_level = cleaned.get('year_level')

        if first_name and last_name and course and year_level:
            duplicate_qs = Student.objects.filter(
                first_name__iexact=first_name,
                last_name__iexact=last_name,
                course=course,
                year_level=year_level,
            )
            if self.instance and self.instance.pk:
                duplicate_qs = duplicate_qs.exclude(pk=self.instance.pk)

            if duplicate_qs.exists():
                raise forms.ValidationError(
                    "A student with the same name, course, and year level already exists. Please review before saving."
                )
        return cleaned

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
    def clean_school_id(self):
        school_id = (self.cleaned_data.get('school_id') or '').strip()
        if not school_id:
            return school_id

        if Student.objects.filter(school_id__iexact=school_id).exists():
            raise forms.ValidationError("This School ID is already registered. Please check your School ID.")
        return school_id

    def clean(self):
        cleaned = super().clean()
        first_name = (cleaned.get('first_name') or '').strip()
        last_name = (cleaned.get('last_name') or '').strip()
        course = cleaned.get('course')
        year_level = cleaned.get('year_level')

        if first_name and last_name and course and year_level:
            already_exists = Student.objects.filter(
                first_name__iexact=first_name,
                last_name__iexact=last_name,
                course=course,
                year_level=year_level,
            ).exists()
            if already_exists:
                raise forms.ValidationError(
                    "A similar student profile already exists in this course and year level. Please contact the admin if this is your record."
                )
        return cleaned

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
