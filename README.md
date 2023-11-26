# IntelliAPI

[![wakatime](https://wakatime.com/badge/user/1980556e-b47a-493f-a376-42da18f2955f/project/d999cab8-ff9b-4e53-bbee-513ad7203f02.svg)](https://wakatime.com/badge/user/1980556e-b47a-493f-a376-42da18f2955f/project/d999cab8-ff9b-4e53-bbee-513ad7203f02)

<!-- # PricePilot - For Educational Purposes Only

🚀 **PricePilot - Your Vehicle Pricing Navigator (Educational Purpose)**

Welcome to PricePilot, a project developed for educational purposes, showcasing the integration of web scraping, data management, and predictive analysis. This project demonstrates how to scrape data from [https://www.lacentrale.fr/](https://www.lacentrale.fr/) and store it in a database, with a focus on predicting car prices using advanced AI algorithms.

## Disclaimer

This project, PricePilot, is intended for educational use only. It serves as a learning tool to demonstrate the concepts of web scraping, data storage, and machine learning. The data scraped from [https://www.lacentrale.fr/](https://www.lacentrale.fr/) is used for educational and demonstrative purposes, and adherence to the website's terms of service and policies is maintained.

**Note**: If this project is accessible via a GitHub repository, please ensure that it is used strictly for educational purposes and in compliance with all applicable laws and regulations.

## Project Overview

PricePilot is a tool designed to predict car prices based on various factors like brand, mileage, and more. It provides a simulated environment for learning about data science and machine learning, particularly in the context of vehicle pricing predictions.

## Setup Instructions

To set up PricePilot for educational purposes, follow these steps:

### 1. Configuration

- Copy the `.env.example` file into a new file named `.env` in both the project root and the `price-pilot` folder:

  ```bash
  cp .env.example .env
  ```

  Fill in the necessary variables in the `.env` files. These files will hold important configuration information for your application.

### 2. Install Backend Requirements

- Ensure you have **Python 3.10** installed. If not, you can download it from [Python Official Website](https://www.python.org/downloads/).
- Install the required dependencies listed in `requirements.txt` using pip in the project root:

  ```bash
  pip install -r requirements.txt
  ```

### 3. Install Frontend Requirements

- Ensure you have **Node.js 18 or higher** installed. If not, you can download it from [Node.js Official Website](https://nodejs.org/).
- Navigate to the `price-pilot` folder and install the frontend dependencies listed in `package.json` using npm:

  ```bash
  cd price-pilot
  npm install
  ```

### 4. Database Configuration

- PricePilot uses MongoDB as the database. Make sure you have MongoDB installed and running or use [MongoAtlas](https://www.mongodb.com/atlas).

### 5. Run Migrations

- Run the database migrations to set up the initial database schema in the project root:

  ```bash
  python manage.py migrate
  ```

### 6. Run the Backend Server

- Start the development server in the project root:

  ```bash
  python manage.py runserver
  ```

### 7. Run the Frontend Server

- Start the frontend server in the `price-pilot` folder:

  ```bash
  npm run dev
  ```

🛫 PricePilot is now ready for takeoff! Access the application at [http://localhost:5173](http://localhost:5173) and explore the world of predicted car prices for educational purposes.

## Key Features

- **Predict Car Prices**: Harness the power of our predictive models to estimate the price of various cars.
- **User-Friendly Interface**: A sleek React-powered frontend ensuring a seamless user experience.
- **Backend Magic with Django and MongoDB**: A robust backend built on Django, fueled by the flexibility of MongoDB.
- **Data-Driven Insights**: Gain insights into trends and patterns that affect used car prices.
- **Open-Source and Collaborative**: Join the community, contribute, and learn the art of predictive algorithms for accurate valuations.

🚗 **Join us on this PricePilot Educational Journey!**

### Frontend

The frontend of PricePilot is located in the `price-pilot` folder. It is a React-powered application with the following key technologies:

- **React**: The UI is built using React, providing an interactive and dynamic user interface.
- **Vite**: Vite is used for fast, efficient development and building of the frontend.

The `package.json` file contains all the necessary dependencies for the frontend. Additionally, an `.env` file is required in the `price-pilot` folder for environment-specific configurations. There's a `price-pilot/.env.example` for reference. -->

## Overview

IntelliAPI is a Django-based REST framework project designed to expose a variety of machine learning models. This project aims to offer a robust, scalable, and user-friendly API interface for interacting with diverse ML algorithms, making them accessible for a wide range of applications.

## Features

- Integration of multiple machine learning models.
- Easy-to-use RESTful endpoints for model interaction.
- Scalable architecture suitable for handling various ML algorithms.
- Customizable model parameters for flexible usage.

## Getting Started

### Prerequisites

- Python 3.x
- Django (latest version)
- Other dependencies listed in `requirements.txt`

### Installation

To set up the IntelliAPI project on your local machine, follow these steps:

```bash
git clone https://github.com/asndiallo/IntelliAPI.git
cd IntelliAPI
pip install -r requirements.txt
```

Set up environment variables as per `.env.example`.

### Running the Server

To run the IntelliAPI server locally:

```bash
python manage.py runserver
```

## Usage

Interact with the API endpoints once the server is running. For example, to predict heart disease:

- Endpoint: `POST http://127.0.0.1:8000/api/v1/heart_disease/predict/`
- Request Body:

  ```json
  {
    "data": {
      "age": 45,
      "sex": 1,
      "cp": 2,
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
  }
  ```

- Optional Parameter: `lang` (can be `en` or `fr`, default is `en`)

- Example body Response:

  ```json
  {
    "prediction": 1,
    "recommendations": {
      "high_fbs": "Assess for potential diabetes management.",
      "high_risk": "Discuss comprehensive cardiovascular risk reduction."
    }
  }
  ```

  <!-- [Provide more specific examples or documentation links for API usage.] -->

## Contributing

Contributions to the IntelliAPI project are welcome. Here's how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<!-- ## Acknowledgments

- [Mention any collaborators, third-party libraries, or other resources you used.] -->

---

For more information or inquiries, please contact <asn.diallo@outlook.com>.

<!-- [Feel free to add any other sections or details you deem necessary.] -->
