import os

from rest_framework import generics, response, status, views

from .models import Car
from .predictor import CarPricePredictor
from .serializers import CarSerializer, UserInputSerializer, serializers


class CarDataView(generics.CreateAPIView):
    """
    A Django REST Framework view that handles the creation of car objects.

    Attributes:
        serializer_class (class): The serializer class used for serializing and deserializing car objects.
        queryset (QuerySet): The queryset of car objects used for the view.
    """

    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarPricePredictionView(views.APIView):
    """
    A view in a Django REST Framework API that handles the prediction of car prices.

    Methods:
    - post: Handles the POST request to the view. It receives the user input data, validates it using the UserInputSerializer, preprocesses the input data, predicts the car price using the CarPricePredictor class, post-processes the prediction, and returns the predicted price to the client.
    """

    def __init__(self):
        """
        Initializes the CarPricePredictionView class.

        Fields:
        - price_pilot: An instance of the CarPricePredictor class that is used to preprocess and predict car prices. It is initialized with a trained model loaded from a file.
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        path = "models/random_forest_model.joblib"
        model_path = os.path.join(current_dir, path)
        self.price_pilot = CarPricePredictor(model_path)

    def post(self, request, format=None):
        """
        Handles the POST request to the view.

        Args:
        - request: The HTTP request object.
        - format: The format of the response.

        Returns:
        - A response object with the predicted car price or validation errors.
        """
        serializer = UserInputSerializer(data=request.data["data"])
        if serializer.is_valid():
            preprocessed_input = self.price_pilot.preprocess_input(
                serializer.validated_data
            )
            prediction = self.price_pilot.predict(preprocessed_input)
            post_process_prediction = self.price_pilot.post_process_prediction(
                prediction
            )
            return response.Response(
                {"predicted_price": post_process_prediction}, status=status.HTTP_200_OK
            )
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarNameSerializer(serializers.ListSerializer):
    child = serializers.CharField()


class CarNameItemSerializer(serializers.Serializer):
    name = serializers.CharField()


class CarDataBulkView(generics.ListCreateAPIView):
    """
    A Django REST Framework view that handles the creation and list of car objects in bulk.

    Attributes:
        serializer_class (class): The serializer class used for serializing and deserializing car objects.
        queryset (QuerySet): The queryset of car objects used for the view.
    """

    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class CarNameListView(views.APIView):
    """
    API view that retrieves all car names from the database, extracts the brand and model information, and returns a list of distinct brand-model pairs to the client.
    """

    def get(self, request, format=None):
        """
        Retrieves all car names from the database, extracts the brand and model information, and returns a list of distinct brand-model pairs to the client.

        Args:
            request: The request object.
            format: The format of the response data (default: None).

        Returns:
            A response containing the list of distinct brand-model pairs.
        """
        car_names = filter(None, Car.objects.values_list("name", flat=True))

        brand_model_pairs = [
            {"brand": brand, "model": model}
            for brand, model in (
                name.split(" ", 1) if " " in name else (name, "") for name in car_names
            )
        ]

        unique_brand_model_pairs = []
        seen_pairs = set()
        for pair in brand_model_pairs:
            pair_tuple = tuple(pair.items())
            if pair_tuple not in seen_pairs:
                seen_pairs.add(pair_tuple)
                unique_brand_model_pairs.append(pair)

        return response.Response(unique_brand_model_pairs, status=status.HTTP_200_OK)
