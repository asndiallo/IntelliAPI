[![wakatime](https://wakatime.com/badge/user/1980556e-b47a-493f-a376-42da18f2955f/project/d999cab8-ff9b-4e53-bbee-513ad7203f02.svg)](https://wakatime.com/badge/user/1980556e-b47a-493f-a376-42da18f2955f/project/d999cab8-ff9b-4e53-bbee-513ad7203f02)

# IntelliAPI

A simple REST API that makes machine learning models accessible through easy-to-use endpoints.

## What it does

IntelliAPI lets you interact with different machine learning models through a REST API. We built it with Django and focused on making it straightforward to use and extend.

## Getting started

### You'll need

- Python 3.x
- Django
- Additional packages listed in `requirements.txt`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/asndiallo/IntelliAPI.git
   cd IntelliAPI
   ```

2. Set up a virtual environment:
   ```bash
   # Using conda
   conda create --name intelliapi_env python=3.10
   conda activate intelliapi_env

   # Or using venv
   python3 -m venv intelliapi_env
   source intelliapi_env/bin/activate  # On Unix/MacOS
   intelliapi_env\Scripts\activate     # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create your environment file:
   - Copy `.env.example` to `.env`
   - Fill in your configuration details

5. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start the server:
   ```bash
   python manage.py runserver
   ```

## How to use it

Check out our [Heart Disease Predictor API guide](heart_disease/README.md#api-endpoints) for a practical example of how to use the API.

## Want to contribute?

We welcome contributions! Here's how:

1. Fork the repository
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Make your changes
4. Commit (`git commit -am 'Add some feature'`)
5. Push to your branch (`git push origin my-new-feature`)
6. Open a Pull Request

## License

MIT License - see [LICENSE](LICENSE) file

---

Questions? Contact me at asn.diallo@outlook.com
