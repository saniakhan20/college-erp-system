from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Marks(models.Model):

    EXAM_TYPES = [
        ('Midterm', 'Midterm'),
        ('Final', 'Final'),
        ('Assignment', 'Assignment'),
        ('Quiz', 'Quiz'),
    ]

    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    faculty = models.ForeignKey('faculty.Faculty', on_delete=models.CASCADE)

    marks_obtained = models.FloatField()
    max_marks = models.FloatField(default=100)

    exam_type = models.CharField(max_length=20, choices=EXAM_TYPES)
    date = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.marks_obtained}"