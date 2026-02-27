from django.db import models
from academics.models import Department
from django.conf import settings

class Faculty(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    designation = models.CharField(max_length=100)
    department = models.ForeignKey('academics.Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
