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
    name = fuzzy.FuzzyText(length=100)
    status = fuzzy.FuzzyChoice([o[0] for o in Bike.STATUS_OPTIONS])
