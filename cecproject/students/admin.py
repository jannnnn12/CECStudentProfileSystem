from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display  = ('full_name', 'course', 'year_level', 'age', 'created_at')
    list_filter   = ('course', 'year_level')
    search_fields = ('first_name', 'last_name', 'course')
    ordering      = ('last_name', 'first_name')
