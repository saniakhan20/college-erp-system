from django.urls import path
from .views import AttendanceCreateView, AttendanceListView, MyAttendanceView

urlpatterns = [
    path('mark/', AttendanceCreateView.as_view()),
    path('all/', AttendanceListView.as_view()),
    path('my-attendance/', MyAttendanceView.as_view()),
]