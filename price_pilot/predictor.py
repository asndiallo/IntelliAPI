import json

import joblib
import numpy as np


class CarPricePredictor:
    def __init__(self, model_path):
        """
        Initializes the CarPricePredictor with the trained model.

        Parameters:
            model_path (str): Path to the trained model.
        """
        self.model = joblib.load(model_path)

    def predict(self, input_data):
        """
        Predicts the car price using the trained model.

        Parameters:
            input_data (dict): Input data containing car features.

        Returns:
            float: Predicted car price.
        """
        try:
            # Reshape the input as the model expects a 2D array
            preprocessed_input = np.array(input_data).reshape(1, -1)

            # Predict using the loaded model
            prediction = self.model.predict(preprocessed_input)[0]

            # Post-process the prediction
            post_processed_prediction = self.post_process_prediction(prediction)

            return post_processed_prediction
        except Exception as e:
            return f"Prediction error: {str(e)}"

    def preprocess_input(self, user_input):
        """
        Preprocesses the input data.

        Parameters:
            user_input (dict): Input data containing car features.

        Returns:
            list: Preprocessed feature values.
        """
        # Define the order of features as in X_train and X_test
        feature_order = [
            "year",
            "power",
            "combined_consumption",
            "mileage",
            "num_doors",
            "num_seats",
            "length",
        ]

        user_input_dict = json.loads(json.dumps(user_input))

        # Extract relevant features from the input
        input_features = [user_input_dict.get(feature, 0) for feature in feature_order]

        # Handle missing or incorrect values (e.g., empty strings, None)
        input_features = [
            0 if feature == "" or feature is None else feature
            for feature in input_features
        ]

        return input_features

    def post_process_prediction(self, prediction):
        """
        Postprocesses the prediction.

        Parameters:
            prediction (float): Predicted car price.

        Returns:
            float: Postprocessed car price.
        """
        # TODO: Implement any postprocessing needed for the prediction
        # For now, let's assume no postprocessing is needed
        return prediction
