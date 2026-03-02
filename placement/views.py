from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdminUserRole, IsStudentUserRole
from .models import Company, JobPosting, Application
from .serializers import CompanySerializer, JobPostingSerializer, ApplicationSerializer

class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsAdminUserRole]

class JobPostingCreateView(generics.CreateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    permission_classes = [IsAuthenticated, IsAdminUserRole]

class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsStudentUserRole]

    def perform_create(self, serializer):
        student = self.request.user.student  # get linked student object
        job = serializer.validated_data['job']

        # Prevent duplicate applications
        if Application.objects.filter(student=student, job=job).exists():
            from rest_framework.exceptions import ValidationError
            raise ValidationError("You have already applied for this job.")

        serializer.save(student=student)