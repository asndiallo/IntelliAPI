import json
import os

from rest_framework import response, status, views

from .constants import FEATURES
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
            shap_explanation = predictor.explain(serializer.validated_data)

            lang = request.query_params.get("lang", "en")
            recommendations = self.generate_recommendations(
                serializer.validated_data, prediction, lang
            )

            return response.Response(
                {
                    "prediction": prediction,
                    "explanation": self.format_shape_values(shap_explanation),
                    "recommendations": recommendations,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return response.Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def generate_recommendations(self, input_data, prediction, lang="en"):
        """
        Generates recommendations based on the input data and the prediction result.
        """
        rec_messages = self.load_recommendations(lang)
        recommendations = {}

        # Blood Pressure
        if input_data["trestbps"] > 140:  # threshold for high blood pressure
            recommendations["high_blood_pressure"] = rec_messages["high_blood_pressure"]

        # Cholesterol Levels
        if input_data["chol"] > 240:  # threshold for high cholesterol
            recommendations["high_cholesterol"] = rec_messages["high_cholesterol"]

        # Fasting Blood Sugar
        if input_data["fbs"] == 1:  # 1 indicates FBS > 120 mg/dl
            recommendations["high_fbs"] = rec_messages["high_fbs"]

        if prediction == 1:
            recommendations["high_risk"] = rec_messages["high_risk"]
        else:
            recommendations["low_risk"] = rec_messages["low_risk"]

        return recommendations

    @staticmethod
    def load_recommendations(lang="en"):
        """
        Loads recommendation messages from a JSON file based on the specified language.
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(
            current_dir, f"recommendations/recommendations_{lang}.json"
        )
        with open(file_path, "r") as file:
            return json.load(file)

    @staticmethod
    def format_shape_values(shap_values):
        """
        Formats the SHAP values to be compatible with the frontend.
        """

        return [
            {"name": FEATURES[i], "shap_value": shap_values[i]}
            for i in range(len(FEATURES))
        ]
