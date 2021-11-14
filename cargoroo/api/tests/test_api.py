import pytest
from django.urls import reverse
from rest_framework import status

from api.tests import factories


@pytest.mark.django_db
class TestAPI:
    def test_fleet_list(self, client):
        factories.FleetFactory()

        response = client.get(reverse('fleet-list'))

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
