from django.urls import path
from .views import CompanyCreateView, ApplicationCreateView, JobPostingCreateView, MyApplicationsView, CompanyListView, JobPostingListView, JobPostingDetailView

urlpatterns = [
    path('companies/create/', CompanyCreateView.as_view()),
    path('jobs/create/', JobPostingCreateView.as_view()),
    path('apply/', ApplicationCreateView.as_view()),
    path('my-applications/', MyApplicationsView.as_view()),
    path('companies/', CompanyListView.as_view()),
    path('jobs/', JobPostingListView.as_view()),
    path('jobs/<int:pk>/', JobPostingDetailView.as_view()),
]