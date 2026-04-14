from django.db import models


YEAR_LEVEL_CHOICES = [
    ('1st Year', '1st Year'),
    ('2nd Year', '2nd Year'),
    ('3rd Year', '3rd Year'),
    ('4th Year', '4th Year'),
    ('Irregular Student', 'Irregular Student'),
]

COURSE_CHOICES = [
    ('BSIT',  'BS Information Technology'),
    ('BSTM',  'BS Tourism Management'),
    ('BSHM',  'BS Hospitality Management'),
    ('BSED',  'BS Education'),
    ('BSCRIM', 'BS Criminology'),
]

STATUS_REASON_CHOICES = [
    ('active', 'Active'),
    ('pending_approval', 'Pending Approval'),
    ('school_transfer', 'School Transfer'),
    ('stopped_school', 'Stopped School'),
    ('other', 'Other'),
]


class Student(models.Model):
    first_name    = models.CharField(max_length=100)
    last_name     = models.CharField(max_length=100)
    age           = models.IntegerField()
    course        = models.CharField(max_length=100, choices=COURSE_CHOICES)
    year_level    = models.CharField(max_length=20,  choices=YEAR_LEVEL_CHOICES)
    school_id     = models.CharField(max_length=50, unique=True)
    email         = models.EmailField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True,
    )
    is_active     = models.BooleanField(default=True)
    status_reason = models.CharField(max_length=20, choices=STATUS_REASON_CHOICES, default='active', blank=True)
    status_note   = models.CharField(max_length=255, blank=True)
    created_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_initials(self):
        return f"{self.first_name[0]}{self.last_name[0]}".upper()
