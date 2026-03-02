from django.urls import path
from .views import FacultyCreateView, FacultyListView, FacultyProfileView

urlpatterns = [
    path('create/', FacultyCreateView.as_view()),
    path('', FacultyListView.as_view()),
    path('profile/', FacultyProfileView.as_view()),
]