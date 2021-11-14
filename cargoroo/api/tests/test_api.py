import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestFleetAPI:
    def test_fleet_list(self, client, fleet):
        response = client.get(reverse('fleet-list'))

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1

    def test_fleet__create(self, client, fleet_json):
        response = client.post(reverse('fleet-list'), fleet_json, format='json')

        assert response.status_code, status.HTTP_201_CREATED
        assert response.data['name'] == fleet_json['name']

        response = client.get(reverse('fleet-list'))
        assert response.data['count'] == 1

    def test_fleet__update(self, client, fleet, fleet_json):
        fleet_json['name'] = 'updated'
        response = client.put(reverse('fleet-detail', kwargs={'pk': fleet.id}), fleet_json, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == 'updated'

    def test_fleet__delete(self, client, fleet):
        response = client.delete(reverse('fleet-detail', kwargs={'pk': fleet.id}), format='json')

        assert response.status_code == status.HTTP_204_NO_CONTENT

        response = client.get(reverse('fleet-list'))
        assert response.data['count'] == 0


@pytest.mark.django_db
class TestBikeAPI:
    def test_bike_list(self, client, bike):
        response = client.get(reverse('bike-list'))

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1

    def test_bike_create(self, client, bike_json, fleet):
        bike_json['fleet'] = fleet.id
        response = client.post(reverse('bike-list'), bike_json, format='json')

        assert response.status_code, status.HTTP_201_CREATED
        assert response.data['properties']['status'] == bike_json['status']

        response = client.get(reverse('bike-list'))
        assert response.data['count'] == 1

    def test_bike_insert_invalid_status(self, client, fleet, bike, bike_json):
        bike_json['status'] = 'updated-status'
        bike_json['fleet'] = fleet.id
        response = client.post(reverse('bike-list'), bike_json, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_bike_update(self, client, fleet, bike, bike_json):
        bike_json['status'] = 'locked'
        bike_json['fleet'] = fleet.id
        response = client.put(reverse('bike-detail', kwargs={'pk': bike.id}), bike_json, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['properties']['status'] == 'locked'

    def test_bike_update_invalid_status(self, client, fleet, bike, bike_json):
        bike_json['status'] = 'updated-status'
        bike_json['fleet'] = fleet.id
        response = client.put(reverse('bike-detail', kwargs={'pk': bike.id}), bike_json, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_bike_delete(self, client, bike):
        response = client.delete(reverse('bike-detail', kwargs={'pk': bike.id}), format='json')

        assert response.status_code == status.HTTP_204_NO_CONTENT

        response = client.get(reverse('bike-list'))
        assert response.data['count'] == 0
