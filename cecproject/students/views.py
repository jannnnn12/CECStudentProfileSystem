from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student
from .forms import StudentForm


# ── Authentication ────────────────────────────────────────────

def login_view(request):
    """Login page with background image."""
    if request.user.is_authenticated:
        return redirect('student_list')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            return redirect('student_list')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'students/login.html')


def logout_view(request):
    """Log out and redirect to login."""
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


# ── Student CRUD ──────────────────────────────────────────────

@login_required
def student_list(request):
    """Dashboard — list all students as cards."""
    query    = request.GET.get('q', '').strip()
    students = Student.objects.all()

    if query:
        students = students.filter(first_name__icontains=query) | \
                   students.filter(last_name__icontains=query)  | \
                   students.filter(course__icontains=query)

    context = {
        'students': students,
        'query':    query,
        'total':    Student.objects.count(),
    }
    return render(request, 'students/student_list.html', context)


@login_required
def student_detail(request, pk):
    """View a single student's full profile."""
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})


@login_required
def student_add(request):
    """Add a new student profile."""
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Profile for {student.full_name()} created successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {
        'form':   form,
        'action': 'Add Student',
        'btn_label': 'Save Profile',
    })


@login_required
def student_edit(request, pk):
    """Edit an existing student profile."""
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profile for {student.full_name()} updated successfully!')
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {
        'form':      form,
        'action':    'Edit Student',
        'btn_label': 'Update Profile',
        'student':   student,
    })


@login_required
def student_delete(request, pk):
    """Confirm and delete a student profile."""
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        name = student.full_name()
        student.delete()
        messages.success(request, f'Profile for {name} has been deleted.')
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})
