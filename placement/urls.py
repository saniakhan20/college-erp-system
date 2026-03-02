from django.urls import path
from .views import CompanyCreateView, ApplicationCreateView, JobPostingCreateView

urlpatterns = [
    path('companies/create/', CompanyCreateView.as_view()),
    path('jobs/create/', JobPostingCreateView.as_view()),
    path('apply/', ApplicationCreateView.as_view()),
]