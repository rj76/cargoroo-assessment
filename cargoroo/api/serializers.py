from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from . import models


class FleetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fleet
        fields = ('id', 'name')


class BikeSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Bike
        geo_field = 'location'
        fields = ('id', 'fleet', 'status', 'location')
