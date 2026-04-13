from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from django.http import HttpRequest
from .models import Student, COURSE_CHOICES, STATUS_REASON_CHOICES
from .forms import StudentForm, StudentRegistrationForm


# ── Helper Functions ──────────────────────────────────────────

def get_registration_url(request: HttpRequest) -> str:
    """Get the full registration URL for QR code."""
    return request.build_absolute_uri('/register/')


# ── Authentication ────────────────────────────────────────────

def login_view(request):
    """Login page with background image and student registration link with QR code."""
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

    # Generate QR code URL for student registration
    registration_url = get_registration_url(request)
    qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={registration_url}"
    
    context = {
        'registration_url': registration_url,
        'qr_code_url': qr_code_url,
    }
    return render(request, 'students/login.html', context)


def logout_view(request):
    """Log out and redirect to login."""
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


# ── Student Registration (Public) ──────────────────────────────

def student_register(request):
    """Public registration form for students."""
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.is_active = True
            student.status_reason = 'active'
            student.save()
            messages.success(request, f'Welcome {student.full_name()}! Your profile has been created successfully. Admin can now see it in the student dashboard.')
            return redirect('student_register_success', pk=student.pk)
    else:
        form = StudentRegistrationForm()
    
    registration_url = get_registration_url(request)
    qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?size=220x220&data={registration_url}"

    context = {
        'form': form,
        'action': 'Student Registration',
        'registration_url': registration_url,
        'qr_code_url': qr_code_url,
    }
    return render(request, 'students/student_register.html', context)


def student_register_success(request, pk):
    """Show success message after registration."""
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_register_success.html', {'student': student})


# ── Student CRUD (Admin) ──────────────────────────────────────

@login_required
def student_list(request):
    """Dashboard — list all students as cards with course filtering and statistics."""
    course_filter = request.GET.get('course', '').strip()
    query = request.GET.get('q', '').strip()
    students = Student.objects.all()

    # Apply course filter
    if course_filter:
        students = students.filter(course=course_filter)

    # Apply search filter
    if query:
        students = students.filter(first_name__icontains=query) | \
                   students.filter(last_name__icontains=query) | \
                   students.filter(school_id__icontains=query)

    # Get course statistics
    course_stats = Student.objects.values('course').annotate(count=Count('course')).order_by('course')

    context = {
        'students': students,
        'query': query,
        'course_filter': course_filter,
        'total': Student.objects.count(),
        'active_count': Student.objects.filter(is_active=True).count(),
        'inactive_count': Student.objects.filter(is_active=False).count(),
        'course_choices': COURSE_CHOICES,
        'course_stats': course_stats,
    }
    return render(request, 'students/student_list.html', context)


@login_required
def student_detail(request, pk):
    """View a single student's full profile."""
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})


@login_required
def student_add(request):
    """Add a new student profile (Admin only)."""
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Profile for {student.full_name()} created successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {
        'form': form,
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
        'form': form,
        'action': 'Edit Student',
        'btn_label': 'Update Profile',
        'student': student,
    })


@login_required
def student_set_inactive(request, pk):
    """Mark a student as inactive with a reason."""
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        reason = request.POST.get('status_reason', 'other')
        student.is_active = False
        student.status_reason = reason
        student.save()
        messages.success(request, f'Profile for {student.full_name()} marked as inactive ({dict(STATUS_REASON_CHOICES).get(reason, reason)}).')
        return redirect('student_list')
    
    return render(request, 'students/student_set_inactive.html', {
        'student': student,
        'status_reasons': STATUS_REASON_CHOICES,
    })


@login_required
def student_set_active(request, pk):
    """Mark a student as active again."""
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        student.is_active = True
        student.status_reason = 'active'
        student.save()
        messages.success(request, f'Profile for {student.full_name()} marked as active.')
        return redirect('student_list')
    
    return render(request, 'students/student_set_active.html', {'student': student})
