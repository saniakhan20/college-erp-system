from django.contrib import admin
from .models import Department, Course, Subject, Marks

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Marks)