from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.db import models


class FleetManager(models.Manager):
    pass


class BikeManager(models.Manager):
    def get_nearest(self, point: Point) -> models.QuerySet:
        qs = self.get_queryset().annotate(distance=Distance('location', point))
        qs = qs.order_by('distance')

        return qs
