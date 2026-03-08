from django.urls import path
from .views import FeeStructureCreateView, PaymentCreateView, MyPaymentsView

urlpatterns = [
    path('fee-structure/create/', FeeStructureCreateView.as_view()),
    path('payment/create/', PaymentCreateView.as_view()),
    path('my-payments/', MyPaymentsView.as_view()),
]