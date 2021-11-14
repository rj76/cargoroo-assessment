from django.contrib.gis.geos import Point
from django.contrib.gis.db.models import PointField
from django.db import models

from . import managers


class Fleet(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)

    objects = managers.FleetManager()


class Bike(models.Model):
    STATUS_OPTIONS = (
        ('locked', 'locked'),
        ('unlocked', 'unlocked'),
    )

    id = models.CharField(max_length=50, primary_key=True)
    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_OPTIONS)
    location = PointField()

    objects = managers.BikeManager()

    def set_location(self, lon, lat):
        self.location = Point(lon, lat)
