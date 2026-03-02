from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


class StudentListCreateView(generics.ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "ADMIN":
            return Student.objects.all()

        elif user.role == "STUDENT":
            return Student.objects.filter(user=user)

        else:
            return Student.objects.none()