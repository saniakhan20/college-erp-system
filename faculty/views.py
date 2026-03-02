from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdminUserRole
from .models import Faculty
from .serializers import FacultySerializer


# Admin can create faculty
class FacultyCreateView(generics.CreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [IsAuthenticated, IsAdminUserRole]


# Admin can list all faculty
class FacultyListView(generics.ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [IsAuthenticated, IsAdminUserRole]


# Faculty can view their own profile
class FacultyProfileView(generics.RetrieveAPIView):
    serializer_class = FacultySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.faculty