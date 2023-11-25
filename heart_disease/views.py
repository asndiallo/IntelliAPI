import os

from rest_framework import response, status, views

from .predictor import HeartDiseasePredictor
from .serializers import UserInputSerializer


class HeartDiseasePredictorView(views.APIView):
    def get_predictor(self):
        """
        Lazily loads and returns the HeartDiseasePredictor instance.
        """
        if not hasattr(self, "_heart_disease_predictor"):
            current_dir = os.path.dirname(os.path.abspath(__file__))
            model_path = os.path.join(
                current_dir, "models/gradient_boosting_model.joblib"
            )
            scaler_path = os.path.join(current_dir, "models/scaler.joblib")
            self._heart_disease_predictor = HeartDiseasePredictor(
                model_path, scaler_path
            )
        return self._heart_disease_predictor

    def post(self, request, *args, **kwargs):
        """
        Handles the POST request to the view.
        """
        serializer = UserInputSerializer(data=request.data.get("data"))
        if serializer.is_valid():
            predictor = self.get_predictor()
            prediction = predictor.predict(serializer.validated_data)

            return response.Response(
                {"prediction": prediction}, status=status.HTTP_200_OK
            )
        else:
            return response.Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )