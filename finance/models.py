from django.db import models
from students.models import Student

class FeeStructure(models.Model):

    department = models.ForeignKey('academics.Department', on_delete=models.CASCADE)
    course = models.ForeignKey('academics.Course', on_delete=models.CASCADE)

    tuition_fee = models.FloatField()
    exam_fee = models.FloatField()
    library_fee = models.FloatField()
    other_fee = models.FloatField(default=0)

    year = models.IntegerField()

    def __str__(self):
        return f"{self.course} - {self.year}"


class Payment(models.Model):

    STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
    ]

    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.CASCADE)

    amount_paid = models.FloatField()
    payment_date = models.DateField()

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student} - {self.amount_paid}"