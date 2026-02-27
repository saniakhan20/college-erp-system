from django.db import models
from students.models import Student

class Fee(models.Model):
    STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
    ]

    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    paid_amount = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    due_date = models.DateField()

    def __str__(self):
        return self.student.enrollment_no