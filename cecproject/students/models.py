from django.db import models


YEAR_LEVEL_CHOICES = [
    ('1st Year', '1st Year'),
    ('2nd Year', '2nd Year'),
    ('3rd Year', '3rd Year'),
    ('4th Year', '4th Year'),
    ('5th Year', '5th Year'),
]

COURSE_CHOICES = [
    ('BSIT',  'BS Information Technology'),
    ('BSTM',  'BS Tourism Management'),
    ('BSHM',  'BS Hospitality Management'),
    ('BSED',  'BS Education'),
    ('BSCRIM', 'BS Criminology'),
]


class Student(models.Model):
    first_name    = models.CharField(max_length=100)
    last_name     = models.CharField(max_length=100)
    age           = models.IntegerField()
    course        = models.CharField(max_length=100, choices=COURSE_CHOICES)
    year_level    = models.CharField(max_length=20,  choices=YEAR_LEVEL_CHOICES)
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_initials(self):
        return f"{self.first_name[0]}{self.last_name[0]}".upper()
