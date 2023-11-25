from django.urls import include, path

urlpatterns = [
    path("heart_disease/", include("heart_disease.urls")),
    path("price_pilot/", include("price_pilot.urls")),
]
