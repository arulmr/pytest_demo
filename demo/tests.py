from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse

import pytest
import requests_mock
from ddf import G

from .models import Person

pytestmark = pytest.mark.django_db


@pytest.fixture
def mock_cat_api():
    with requests_mock.Mocker(json_encoder=DjangoJSONEncoder) as m:
        m.register_uri('GET', 'https://catfact.ninja/fact', json={'fact': 'This is a cat fact.', 'length': 19})


@pytest.fixture
def generate_100_person_objs():
    # Using Django dynamic fixtures to generate 100 records at once. Values will be randomly generated.
    G(Person, n=100)
    return Person.objects.all().order_by('-created_at')


class TestPersonsView:
    def test_person_view(self, client):
        # Making a get request to the persons view
        get_response = client.get(reverse('persons'))
        assert get_response.status_code == 200  # URL is reachable
        assert not get_response.context['persons_list'] # No person object exists (checking in context)
        assert not Person.objects.count()  # No person object exists (checking in DB)

        # Making a post request to the persons view with post data
        response = client.post(reverse('persons'), {'first_name': 'John', 'last_name': 'Doe'})

        # Asserting we got a 200 response for the post request
        assert response.status_code == 200
        assert Person.objects.count() == 1  # One person object is created

        person_1 = Person.objects.first()  # Getting the recently created person object
        # Checking the values in the 1st created object
        assert person_1.first_name == 'John'
        assert person_1.last_name == 'Doe'
        assert person_1.full_name == 'John Doe'

        # Making a 2nd post request to the persons view with post data
        response = client.post(reverse('persons'), {'first_name': 'Jane', 'last_name': 'Doe'})

        # Asserting we got a 200 response for the post request
        assert response.status_code == 200
        assert Person.objects.count() == 2  # 2nd person object is also created

        person_2 = Person.objects.last()  # Getting the recently created person object
        # Checking the values in the 2nd created object
        assert person_2.first_name == 'Jane'
        assert person_2.last_name == 'Doe'
        assert person_2.full_name == 'Jane Doe'

        # Querysets can't be compared. So converting them to list and asserting
        assert list(response.context['persons_list']) == list(Person.objects.all().order_by('-created_at'))

    def test_persons_list(self, client, generate_100_person_objs):
        assert Person.objects.count() == 100
        response = client.get(reverse('persons'))
        assert list(response.context['persons_list']) == list(generate_100_person_objs)


class TestCatApiView:
    def test_cat_api_view(self, client, requests_mock):
        # Registering a mock response for the API call
        requests_mock.register_uri('GET', 'https://catfact.ninja/fact', json={'fact': 'This is a cat fact.', 'length': 19})

        # Making a call to the view which will then call the API and receive the mock response
        response = client.get(reverse('cat_api'))
        assert response.status_code == 200
        assert response.context['data']['fact'] == 'This is a cat fact.'
        assert response.context['data']['length'] == 19


def test_admin_user_login(admin_client):
    # admin_client will be logged in as a superuser by default. Superuser will be created if it doesn't exist.
    response = admin_client.get('/admin/')
    assert response.wsgi_request.user.is_superuser


def test_user_login(client):
    # client will not be logged in by default.
    response = client.get('/admin/')
    assert not response.wsgi_request.user.id  # Anonymous user

    # Creating an user
    user = User.objects.create_superuser(
        'superuser',
        email='superuser@example.com',
        password='login-secret',
    )

    # Logging in as the created user
    client.login(username='superuser', password='login-secret')
    response = client.get('/admin/')

    # Assert the current user
    assert response.wsgi_request.user == user

    # Logout from the current user
    client.logout()

    # Assert no user is logged in.
    response = client.get('/admin/')
    assert not response.wsgi_request.user.id  # Anonymous user
