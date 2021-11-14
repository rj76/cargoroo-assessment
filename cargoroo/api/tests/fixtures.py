import pytest
from django.contrib.gis.geos import Point
from rest_framework.test import APIClient

from api.batch import Batch
from api.tests import factories


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def batch():
    return Batch()


@pytest.fixture
def fleet_json():
    return {
        "id": "FL_003",
        "name": "Utrecht"
    }


@pytest.fixture
def bike_json():
    return {
        "id": "BK_001",
        "fleet": "FL_001",
        "status": "unlocked",
        "location": {
            "type": "Point",
            "coordinates": [52.08466738004343, 4.3185523728791075],
        },
    }


@pytest.fixture
def bike():
    return factories.BikeFactory()


@pytest.fixture
def bike2():
    bike = factories.BikeFactory(
        location=Point(52.36623489297726, 4.918148840679546)
    )

    return bike


@pytest.fixture
def fleet():
    return factories.FleetFactory()
