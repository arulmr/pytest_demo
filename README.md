# Pytest Demo
This Django project contains basic Pytest tests covering:
 - Pytest fixtures.
 - Making requests to internal URLs using Pytest client.
 - Generating DB data using Django dynamic fixtures.
 - Mocking external API calls.
 - User login.
 - Admin user.
 - Pytest coverage report.

Inline comments are given in the tests for better understanding.

# Packages and Versions Used
 - Python 3.8.10
 - Django 4.1.3
 - [Django Dynamic Fixture 3.1.2](https://django-dynamic-fixture.readthedocs.io/en/latest/)
 - [pytest-django 4.5.2](https://pytest-django.readthedocs.io/en/latest/index.html)
 - [pytest-cov 4.0.0](https://pytest-cov.readthedocs.io/en/latest/)
 - [requests-mock 1.10.0](https://requests-mock.readthedocs.io/en/latest/)

# Setup
1. Clone the repo.
2. Create a virtual environment.
3. Install requirements using the command `pip install -r requirements.txt`.
4. Apply DB migrations using the command `python manage.py migrate`.
5. Run the application using the command `python manage.py runserver`.
6. Refer [urls.py](pytest_demo/urls.py) for the available URLs.

# Commonly Used Pytest Commands
1. Running pytest:
```python
pytest
```

2. Running specific pytest test case:
```python
# Running specific test class
pytest -k TestSampleClass

# Running specific individual function or a function inside a test class
pytest -k test_sample_function
```

3. Running pytest with detailed output:
```python
pytest -v
```

4. Running pytest with print statements or to use [pdb](https://www.geeksforgeeks.org/python-debugger-python-pdb/):
```python
pytest -s
```

5. To get [pytest coverage](https://pytest-cov.readthedocs.io/en/latest/):
```python
pytest --cov=demo/

# Sample output
❯ pytest --cov=demo/
=============================================================== test session starts ================================================================
platform linux -- Python 3.8.10, pytest-7.2.0, pluggy-1.0.0
django: settings: pytest_demo.settings (from ini)
rootdir: /home/arul/git/pytest_demo, configfile: pytest.ini
plugins: requests-mock-1.10.0, django-4.5.2, cov-4.0.0
collected 5 items

demo/tests.py .....                                                                                                                          [100%]

---------- coverage: platform linux, python 3.8.10-final-0 -----------
Name                              Stmts   Miss  Cover
-----------------------------------------------------
demo/__init__.py                      0      0   100%
demo/admin.py                         1      0   100%
demo/apps.py                          4      0   100%
demo/forms.py                        10      0   100%
demo/migrations/0001_initial.py       5      0   100%
demo/migrations/__init__.py           0      0   100%
demo/models.py                       13      1    92%
demo/tests.py                        61      2    97%
demo/views.py                        15      0   100%
-----------------------------------------------------
TOTAL                               109      3    97%


================================================================ 5 passed in 4.29s =================================================================
```

6. Generate [pytest coverage report](https://pytest-cov.readthedocs.io/en/latest/reporting.html) in HTML format:
```python
pytest --cov-report html --cov=demo/
```
[Sample HTML report](https://sample-pytest-cov.surge.sh)
