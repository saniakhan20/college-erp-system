from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsFacultyUserRole
from .models import Attendance
from .serializers import AttendanceSerializer


# Faculty marks attendance
class AttendanceCreateView(generics.CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated, IsFacultyUserRole]


# Admin view all attendance
class AttendanceListView(generics.ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]


# Student view own attendance
class MyAttendanceView(generics.ListAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "STUDENT":
            return Attendance.objects.filter(student=user.student)

        if user.role == "ADMIN":
            return Attendance.objects.all()

        return Attendance.objects.none()