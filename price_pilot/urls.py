from django.urls import path

from .views import CarDataBulkView, CarDataView, CarNameListView, CarPricePredictionView

urlpatterns = [
    path("car_data/", CarDataView.as_view(), name="car_data"),
    path("predict_price/", CarPricePredictionView.as_view(), name="predict_price"),
    path("car_names/", CarNameListView.as_view(), name="car_names"),
    path("car_data_bulk/", CarDataBulkView.as_view(), name="car_data_bulk"),
]
