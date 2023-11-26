# Heart Disease Predictor API

## Overview

The Heart Disease Predictor API is a Django-based RESTful service designed to predict the likelihood of heart disease based on clinical parameters. Utilizing a Gradient Boosting model trained on the UCI Heart Disease dataset, this API offers healthcare professionals a robust and user-friendly interface for heart disease risk assessment.

## Getting Started

### Prerequisites

- Python 3.10
- Django
- Django REST Framework
- Other dependencies listed in project's `requirements.txt`

### Installation

Please follow the installation process described in the [project's documentation](../README.md#installation)

## Usage

### API Endpoints

#### Predict Heart Disease

- **URL**: `/api/v1/heart_disease/predict/`
- **Method**: `POST`
- **Data Params**:

  ```json
  {
      "data": {
          "age": [integer],
          "sex": [0 or 1],
          "cp": [integer],
          "trestbps": [integer],
          "chol": [integer],
          "fbs": [0 or 1],
          "restecg": [integer],
          "thalach": [integer],
          "exang": [0 or 1],
          "oldpeak": [float],
          "slope": [integer],
          "ca": [integer],
          "thal": [integer]
      }
  }
  ```

- Optional Parameter: `lang` (can be `en` or `fr`, default is `en`)

- **Success Response**:

  - **Code**: 200 OK
  - **Content**:

    ```json
    {
        "prediction": [0 or 1],
        "explanation": [
            {
                "feature_name": "string",
                "shap_value": "float"
            },
            ...
        ],
        "recommendations": {
            "key": "string"
        }
    }
    ```

#### Response Field Explanations

- **`prediction`**: Indicates the model's prediction for heart disease. A value of `1` suggests a higher likelihood of heart disease, while `0` indicates a lower likelihood.

- **`explanation`**: This field contains an array of objects, each representing a feature used in the prediction model and its corresponding SHAP value. SHAP (SHapley Additive exPlanations) values explain the impact of each feature on the model's output. Here's how to interpret these values:

  - A positive SHAP value indicates that the feature contributes to increasing the likelihood of the predicted outcome (e.g., higher risk of heart disease).
  - A negative SHAP value suggests that the feature contributes to decreasing the likelihood of the predicted outcome.
  - The magnitude of the SHAP value signifies the strength of the feature's impact. Larger absolute values mean greater influence.

- **`recommendations`**: Provides actionable health recommendations based on the prediction results. These are tailored to the specific features of the patient's profile and the model's prediction. The recommendations are also language-specific, based on the optional `lang` parameter.

- **Error Response**:

  - **Code**: 400 BAD REQUEST
  - **Content**:

    - The response will contain specific error messages for each invalid data field. For example, if a string is submitted instead of an integer for a field like `slope`, the response would be:

      ```json
      {
        "slope": ["A valid integer is required."]
      }
      ```

    - Each field in the data payload will have its own error message in case of invalid input, providing clear guidance on what needs to be corrected.

### Sample Request

To utilize the Heart Disease Predictor API, send a POST request to the `/api/v1/heart_disease/predict/` endpoint with clinical parameters as data inputs. This request returns a prediction indicating the likelihood of heart disease, along with a detailed breakdown of how each input parameter (like age, cholesterol levels, etc.) affects the prediction. Additionally, the response includes health recommendations that are pertinent to the prediction outcome.

Below is an example of how to make this request using `curl`:

```bash
curl -X POST http://localhost:8000/api/v1/heart_disease/predict/ \
     -H 'Content-Type: application/json' \
     -d '{
            "data": {
                "age": 45,
                "sex": 1,
                "cp": 1,
                "trestbps": 120,
                "chol": 240,
                "fbs": 1,
                "restecg": 1,
                "thalach": 150,
                "exang": 0,
                "oldpeak": 2.3,
                "slope": 2,
                "ca": 0,
                "thal": 2
            }
         }'
```

This example shows a request for a 45-year-old individual with specific clinical parameters. Replace these values with actual patient data to get a corresponding prediction and recommendations.

## Features

- **Heart Disease Prediction**: Using clinical parameters to predict the likelihood of heart disease.
- **SHAP Value Analysis**: Provides SHAP values for each prediction to understand feature impact.
- **Multilingual Support**: Recommendations available in multiple languages.

## Recommendations

Based on the prediction, the API offers tailored health recommendations. These are language-specific and based on current clinical guidelines.

## Contributing

Contributions to the Heart Disease Predictor API are welcome. Please ensure to follow the [project](../README.md#contributing)'s coding standards and pull request guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## Contact

For any queries or issues, please contact me at <asn.diallo@outlook.com>.

## Acknowledgments

- [UCI Machine Learning Repository for the Heart Disease Dataset](https://archive.ics.uci.edu/dataset/45/heart+disease).
- Django and Django REST Framework communities.
