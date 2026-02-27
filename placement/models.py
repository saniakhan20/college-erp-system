from django.db import models
from students.models import Student
from academics.models import Department

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    package = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name


class JobPosting(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    min_cgpa = models.FloatField()
    allowed_departments = models.ManyToManyField(Department)
    deadline = models.DateField()

    def __str__(self):
        return self.role


class Application(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Shortlisted', 'Shortlisted'),
        ('Rejected', 'Rejected'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student} - {self.job}"