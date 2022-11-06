from django.shortcuts import render

import requests

from demo.forms import PersonForm
from demo.models import Person


def persons(request):
    form = PersonForm()

    if request.method == 'POST':
        new_person = PersonForm(request.POST)
        new_person.save()

    persons_list = Person.objects.all()

    return render(request, 'person.html', locals())


def cat_api(request):
    response = requests.get('https://catfact.ninja/fact')
    data = response.json()
    return render(request, 'cat_api.html', locals())
