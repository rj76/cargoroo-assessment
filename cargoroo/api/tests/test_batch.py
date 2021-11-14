import pytest

from api import models


@pytest.mark.django_db
def test_batch(batch):
    batch.run()

    assert models.Fleet.objects.count() == 3
    assert models.Bike.objects.count() == 9
