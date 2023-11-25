from django.urls import path

from .views import HeartDiseasePredictorView

urlpatterns = [
    path("predict/", HeartDiseasePredictorView.as_view(), name="predict"),
]
