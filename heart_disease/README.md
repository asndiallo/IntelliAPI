# Heart Disease Predictor API

## Overview

The Heart Disease Predictor API is a Django-based RESTful service designed to predict the likelihood of heart disease based on clinical parameters. Utilizing a Gradient Boosting model trained on the UCI Heart Disease dataset, this API offers healthcare professionals a robust and user-friendly interface for heart disease risk assessment.

## Getting Started

### Prerequisites

- Python 3.x
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
        "explanation": [object],
        "recommendations": [object]
    }
    ```

- **Error Response**:
  - **Code**: 400 BAD REQUEST
  - **Content**: `{ "detail": "Invalid data." }`

### Sample Request

```bash
curl -X POST http://localhost:8000/api/v1/heart_disease/predict/ \
     -H 'Content-Type: application/json' \
     -d '{"data": {"age": 45, "sex": 1, "cp": 1, "trestbps": 120, "chol": 240, "fbs": 1, "restecg": 1, "thalach": 150, "exang": 0, "oldpeak": 2.3, "slope": 2, "ca": 0, "thal": 2}}'
```

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
