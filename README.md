# Pytest Demo
This Django project contains basic Pytest tests covering:
 - Pytest fixtures.
 - Making requests to internal URLs using Pytest client.
 - Generating DB data using Django dynamic fixtures.
 - Mocking external API calls.
 - User login.
 - Admin user.

Inline comments are given in the tests for better understanding.

# Packages and Versions Used
 - Python 3.8.10
 - Django 4.1.3
 - [Django Dynamic Fixture 3.1.2](https://django-dynamic-fixture.readthedocs.io/en/latest/)
 - [pytest-django 4.5.2](https://pytest-django.readthedocs.io/en/latest/index.html)
 - [requests-mock 1.10.0](https://requests-mock.readthedocs.io/en/latest/)

# Setup
1. Clone the repo.
2. Create a virtual environment.
3. Install requirements using the command `pip install -r requirements.txt`.
4. Apply DB migrations using the command `python manage.py migrate`.
5. Run the application using the command `python manage.py runserver`.
6. Refer [urls.py](pytest_demo/urls.py) for the available URLs.
