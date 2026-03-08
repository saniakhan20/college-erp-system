from django.urls import path
from .views import UploadMarksView, AllMarksView, MyMarksView

urlpatterns = [
    path('upload/', UploadMarksView.as_view()),
    path('all/', AllMarksView.as_view()),
    path('my-marks/', MyMarksView.as_view()),
]