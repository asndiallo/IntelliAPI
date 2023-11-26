import joblib
import pandas as pd
import shap

from .constants import FEATURES


class HeartDiseasePredictor:
    def __init__(self, model_path, scaler_path):
        """
        Initializes the HeartDiseasePredictor with the trained model and scaler.
        """
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)

    def predict(self, input_data):
        """
        Predicts the cardiovascular risk using the trained model.
        """
        try:
            preprocessed_input = self.preprocess_input(input_data, self.scaler)
            prediction = self.model.predict(preprocessed_input)
            return self.post_process_prediction(prediction)
        except Exception as e:
            print(f"Prediction error: {str(e)}")
            return None

    def explain(self, input_data):
        """
        Explains the model's prediction using SHAP.
        """
        try:
            preprocessed_input = self.preprocess_input(input_data, self.scaler)
            explainer = shap.TreeExplainer(self.model)
            shap_values = explainer.shap_values(preprocessed_input)
            return shap_values[0]
        except Exception as e:
            print(f"Explanation error: {str(e)}")
            return None

    @staticmethod
    def preprocess_input(input_data, scaler):
        """
        Preprocesses the input data to the format required by the model.
        """
        df = pd.DataFrame([input_data], columns=FEATURES)
        scaled_data = scaler.transform(df)
        return scaled_data

    @staticmethod
    def post_process_prediction(prediction):
        """
        Post-processes the model's prediction to interpret the result.
        """
        # TODO: Implement any postprocessing needed for the prediction
        return prediction[0]
