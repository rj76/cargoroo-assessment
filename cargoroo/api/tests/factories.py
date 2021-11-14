from django.contrib.gis.geos import Point
from factory import fuzzy, django, SubFactory

from api.models import Fleet, Bike


class FleetFactory(django.DjangoModelFactory):
    class Meta:
        model = Fleet

    id = fuzzy.FuzzyText(length=10)
    name = fuzzy.FuzzyText(length=100)


class BikeFactory(django.DjangoModelFactory):
    class Meta:
        model = Bike

    id = fuzzy.FuzzyText(length=10)
    fleet = SubFactory(FleetFactory)
    status = fuzzy.FuzzyChoice([o[0] for o in Bike.STATUS_OPTIONS])
    location = Point(52.09398461023647, 4.3185523728791075)
