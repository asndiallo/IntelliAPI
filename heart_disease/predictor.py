import joblib
import pandas as pd

FEATURES = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
]


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
