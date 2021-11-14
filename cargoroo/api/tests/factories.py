from factory import fuzzy, django

from api.models import Fleet


class FleetFactory(django.DjangoModelFactory):
    class Meta:
        model = Fleet

    id = fuzzy.FuzzyText(length=10)
    name = fuzzy.FuzzyText(length=100)
