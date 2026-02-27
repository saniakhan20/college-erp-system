from django.db import models
from academics.models import Department, Course
from django.conf import settings

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    enrollment_no = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    cgpa = models.FloatField()
    department = models.ForeignKey('academics.Department', on_delete=models.CASCADE)
    course = models.ForeignKey('academics.Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.enrollment_no