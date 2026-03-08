from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdminUserRole
from .models import FeeStructure, Payment
from .serializers import FeeStructureSerializer, PaymentSerializer


# Admin creates fee structure
class FeeStructureCreateView(generics.CreateAPIView):

    queryset = FeeStructure.objects.all()
    serializer_class = FeeStructureSerializer
    permission_classes = [IsAuthenticated, IsAdminUserRole]


# Admin records payment
class PaymentCreateView(generics.CreateAPIView):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsAdminUserRole]


# Student views their payments
class MyPaymentsView(generics.ListAPIView):

    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user

        if user.role == "STUDENT":
            return Payment.objects.filter(student=user.student)

        if user.role == "ADMIN":
            return Payment.objects.all()

        return Payment.objects.none()