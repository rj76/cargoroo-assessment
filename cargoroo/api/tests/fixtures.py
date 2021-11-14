import pytest
from rest_framework.test import APIClient

from api.batch import Batch


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def batch():
    return Batch()
