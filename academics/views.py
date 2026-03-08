from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsFacultyUserRole
from .models import Marks
from .serializers import MarksSerializer


# Faculty uploads marks
class UploadMarksView(generics.CreateAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer
    permission_classes = [IsAuthenticated, IsFacultyUserRole]


# Admin views all marks
class AllMarksView(generics.ListAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer
    permission_classes = [IsAuthenticated]


# Student views their marks
class MyMarksView(generics.ListAPIView):

    serializer_class = MarksSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "STUDENT":
            return Marks.objects.filter(student=user.student)

        if user.role == "ADMIN":
            return Marks.objects.all()

        return Marks.objects.none()