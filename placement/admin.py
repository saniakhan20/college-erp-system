from django.contrib import admin
from .models import Company, JobPosting, Application

admin.site.register(Company)
admin.site.register(JobPosting)
admin.site.register(Application)
